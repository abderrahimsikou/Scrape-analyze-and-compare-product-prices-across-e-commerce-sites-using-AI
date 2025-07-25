# Add Cleaned Dataset to PostgreSQL

from sqlalchemy import create_engine, Table, MetaData, Column, Float, Integer
from dotenv import load_dotenv
import urllib.parse
import os
import pandas as pd

# Read Dataset
data = pd.read_csv('Data/Cleaning_DataSet.csv')

# Connect with Database
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

password_encoded = urllib.parse.quote_plus(DB_PASSWORD)

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{password_encoded}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# Create Table In PostgreSQL
table_data = MetaData()

ecommerce_jumia_data_cleaned = Table(
    'ecommerce_jumia_data_cleaned', table_data,
    Column('price', Float),
    Column('original_price', Float),
    Column('discount', Float),
    Column('review_count', Float),
    Column('category', Integer),
    Column('official_store', Float)
)

try:
    table_data.create_all(engine)
except Exception as error:
    print(error)

# Insert CSV Data Into Table
with engine.begin() as conn:
    conn.execute(ecommerce_jumia_data_cleaned.insert(), data.to_dict(orient='records'))