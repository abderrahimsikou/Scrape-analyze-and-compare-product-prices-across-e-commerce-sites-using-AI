# Scrape, analyze and compare product prices across e-commerce sites using AI

## Description

From web scraping to data cleaning, data visualization, machine learning, and SQL databases, this project uses cutting-edge data science techniques to analyze and predict e-commerce products.

This is a complete end-to-end data science project where I collect, clean, analyze, and model product data from e-commerce websites, with the goal of predicting product prices and analyzing patterns across categories and sellers using Machine Learning


## 🔍 Project Objectives

- 🕸️ Web Scraping     : Scrape product data from the Jumia e-commerce site across multiple categories.
- 🧹 Data Cleaning    : Clean and preprocess the scraped data (handling missing values, formatting prices, encoding categories).
- 📊 Data Analyze     : Analyze the product prices and trends using visualization tools.
- 🤖 Machine Learning : Train Machine Learning models to predict the actual price of a product based on its features (original price, discount, category, etc.).
- 🧪 Model Evaluation : Evaluate and compare models (Linear Regression, Random Forest, etc.) using GridSearchCV.
- 💾 SQL Database     : Store data in PostgreSQL and demonstrate SQL integration.


## 🤖 Machine Learning Pipeline

- Cleaned data (price formatting, missing values)
- Encoded categorical features
- Trained models on features like "original_price", "discount", "review_count", "category"
- Tuned models with "GridSearchCV"
- Evaluated using MAE, RMSE, R²


## 🎯 Results

- Best performing model: Random Forest Regressor
- Model R² Score: 83%
- Visualizations show clear correlation between discount & final price


## 🚀 Project Structure

- Scraping_Data.py : This file content the code of scraping data from jumia website
- Main.ipynb       : This file content the code of Data_Cleaning , Data_visualization, Machine Learning, GridSearchCV
- SQL_DataBase     : This file content the code of connect to database in postgreSQl, Create table in database and insert the cleaning data
- Data             : This folder content the original scraping dataset from web scraping and the cleaning dataset after preprocess
- Model            : This folder content the "Model.pkl" and "StandardScaler.pkl"


## 📦 Tools & Technologies Used

- Web Scraping     :  Selenium, urljoin
- Data Handling    : Pandas
- Visualization    : Seaborn, Matplotlib
- Machine Learning : scikit-learn
- Database         : PostgreSQL, SQLAlchemy


