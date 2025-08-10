from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
DRIVER_URL = os.getenv("DRIVER_URL")

def get_price(driver_url):
    # Paramètrage du webdriver chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)

    # Rattachement des options chrome à notre driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(DRIVER_URL)

    price_whole = driver.find_element(By.CLASS_NAME,'a-price-whole').get_attribute("innerText").replace(",","")
    price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").get_attribute("innerText")
    price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").get_attribute("innerText")

    price_final = float(price_whole) + (float(price_fraction) / 100)
    print(f'The price is of your article is {price_final}{price_symbol}')

    #driver.close() #ferme la fenêtre
    driver.close() #ferme tous les onglets

get_price(DRIVER_URL)