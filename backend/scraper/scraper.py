# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import json
# import time
# import re

# CATEGORY_URLS = [
#     "https://www.wegetanystock.com/baby-care",
#     "https://www.wegetanystock.com/biscuits-snacks-sweets",
#     "https://www.wegetanystock.com/drinks",
#     "https://www.wegetanystock.com/frozen-foods",
#     "https://www.wegetanystock.com/grocery",
#     "https://www.wegetanystock.com/non-foods",
#     "https://www.wegetanystock.com/pet-care"
# ]

# PRODUCT_LIMIT_PER_CATEGORY = 20

# def get_category_name(url):
#     slug = url.rstrip("/").split("/")[-1]
#     return slug.replace("-", " ").title()

# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-blink-features=AutomationControlled")

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#     options=options
# )

# final_data = []

# for url in CATEGORY_URLS:
#     category_name = get_category_name(url)
#     print(f"\n Scraping category: {category_name}")

#     driver.get(url)
#     time.sleep(8)

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)

#     cards = driver.find_elements(By.CSS_SELECTOR, "article.text-gray-700")
#     print(f"Found {len(cards)} cards")

#     products = []

#     for card in cards:
#         if len(products) >= PRODUCT_LIMIT_PER_CATEGORY:
#             break

#         try:
#             name = card.find_element(By.CSS_SELECTOR, "h4").text
#             image = card.find_element(By.TAG_NAME, "img").get_attribute("src")

#             spans = card.find_elements(By.TAG_NAME, "span")
#             volume = ""
#             for span in spans:
#                 if re.search(r"\d+\s*[x×]\s*\d+\s*(ml|g)", span.text.lower()) or \
#                    re.search(r"\d+\s*(ml|g)", span.text.lower()):
#                     volume = span.text
#                     break

#             products.append({
#                 "original_name": name,
#                 "volume": volume,
#                 "image": image
#             })

#         except:
#             continue

#     final_data.append({
#         "category": category_name,
#         "category_url": url,
#         "products": products
#     })

# driver.quit()

# with open("category_products.json", "w", encoding="utf-8") as f:
#     json.dump(final_data, f, indent=4, ensure_ascii=False)

# print("\n ALL CATEGORIES SCRAPED SUCCESSFULLY")

import os
import json
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

CATEGORY_URLS = [
    "https://www.wegetanystock.com/baby-care",
    "https://www.wegetanystock.com/biscuits-snacks-sweets",
    "https://www.wegetanystock.com/drinks",
    "https://www.wegetanystock.com/frozen-foods",
    "https://www.wegetanystock.com/grocery",
    "https://www.wegetanystock.com/non-foods",
    "https://www.wegetanystock.com/pet-care"
]

PRODUCT_LIMIT_PER_CATEGORY = 15

def get_category_name(url):
    slug = url.rstrip("/").split("/")[-1]
    return slug.replace("-", " ").title()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "..", "data", "raw")
FILE_PATH = os.path.join(RAW_DIR, "category_products.json")

os.makedirs(RAW_DIR, exist_ok=True)

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

final_data = []

for url in CATEGORY_URLS:
    category_name = get_category_name(url)
    print(f"\nScraping category: {category_name}")

    driver.get(url)
    time.sleep(8)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    cards = driver.find_elements(By.CSS_SELECTOR, "article.text-gray-700")
    print(f"Found {len(cards)} cards")

    products = []

    for card in cards:
        if len(products) >= PRODUCT_LIMIT_PER_CATEGORY:
            break

        try:
            name = card.find_element(By.CSS_SELECTOR, "h4").text
            image = card.find_element(By.TAG_NAME, "img").get_attribute("src")

            spans = card.find_elements(By.TAG_NAME, "span")
            volume = ""
            for span in spans:
                if re.search(r"\d+\s*[x×]\s*\d+\s*(ml|g)", span.text.lower()) or \
                   re.search(r"\d+\s*(ml|g)", span.text.lower()):
                    volume = span.text
                    break

            products.append({
                "original_name": name,
                "volume": volume,
                "image": image
            })

        except:
            continue

    final_data.append({
        "category": category_name,
        "category_url": url,
        "products": products
    })

driver.quit()

with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4, ensure_ascii=False)

print("\nALL CATEGORIES SCRAPED & SAVED TO data/raw SUCCESSFULLY")
