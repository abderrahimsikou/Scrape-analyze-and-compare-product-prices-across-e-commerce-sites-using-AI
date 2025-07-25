# Scraping Ecommerce Data From Jumia WebSite

# Upload Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import pandas as pd
import time
import random

# Browser Settings
options = Options()
options.add_argument('--headless')  # Run Browser In The background
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# start Runing Browser
driver = webdriver.Chrome(options=options)

base_url = "https://www.jumia.ma"
categories = {
    'beaute-sante': 'https://www.jumia.ma/beaute-hygiene-sante/',
    'mode-male': 'https://www.jumia.ma/vetements-hommes/',
    'mode-female': 'https://www.jumia.ma/vetements-femme/',
    'mode-kids': 'https://www.jumia.ma/mode-mode-enfant/',
    'video-games': 'https://www.jumia.ma/jeux-videos-consoles/',
}

data = []

for category_name, category_url in categories.items():
    print(f"{category_name}")
    
    for page in range(1, 10): 
        print(f"Upload Page {page}")
        driver.get(f"{category_url}?page={page}")
        
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.prd"))
            )
            time.sleep(random.uniform(2, 3))  

            products = driver.find_elements(By.CSS_SELECTOR, "article.prd")

            for p in products:
                product_data = {
                    "name": "",
                    "price": "",
                    "original_price": "",
                    "discount": "",
                    "review_count": "0",
                    "seller": "Jumia",
                    "availability": "Available", 
                    "badges": [],
                    "link": "",
                    "category": category_name 
                }

                # Extract Data
                try:
                    product_data["name"] = p.find_element(By.CSS_SELECTOR, "h3.name").text.strip()
                except:
                    pass

                try:
                    product_data["price"] = p.find_element(By.CSS_SELECTOR, "div.prc").text.strip()
                except:
                    pass

                try:
                    product_data["original_price"] = p.find_element(By.CSS_SELECTOR, "div.old").text.strip()
                except:
                    pass

                try:
                    product_data["discount"] = p.find_element(By.CSS_SELECTOR, "div.bdg._dsct").text.strip()
                except:
                    pass

                try:
                    product_data["review_count"] = p.find_element(By.CSS_SELECTOR, "div.rev").text.strip().split()[0]
                except:
                    pass

                try:
                    product_data["seller"] = p.find_element(By.CSS_SELECTOR, "div.seller").text.strip()
                except:
                    pass

                try:
                    product_data["badges"] = [badge.text.strip() for badge in p.find_elements(By.CSS_SELECTOR, "div.bdg")]
                except:
                    pass

                try:
                    product_data["link"] = urljoin(base_url, p.find_element(By.CSS_SELECTOR, "a.core").get_attribute("href").strip())
                except:
                    pass

                # Add Data
                if product_data["name"] and product_data["price"]:
                    data.append(product_data)

        except Exception as e:
            print(f"Error While Upload Page{page}: {str(e)}")
            continue
driver.quit()

# Save Data
df = pd.DataFrame(data)
df.to_csv("dataset2.csv", index=False, encoding='utf-8-sig')