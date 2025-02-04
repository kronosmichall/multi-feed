# from celery import  Celery

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from dotenv import load_dotenv
from os import getenv
import psycopg2
import asyncio

# Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# WebDriver service
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)

def scrape_ig(amount):
    login = getenv("IGLOGIN")
    password = getenv("IGPASS")

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    allow_cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Allow')]")
    allow_cookies.click()

    login_el = driver.find_element(By.CSS_SELECTOR, "input[aria-label=\"Phone number, username, or email\"]")
    login_el.send_keys(login)
    pass_el = driver.find_element(By.CSS_SELECTOR, "input[aria-label=\"Password\"]")
    pass_el.send_keys(password)

    submit = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    submit.click()
    time.sleep(5)

    # logged in
    driver.get("https://www.instagram.com/explore")
    time.sleep(5)

    urls = set()
    while len(urls) < amount:
        elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '/p/')]")
        for element in elements:
            urls.add(element.get_attribute("href"))
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    shortUrls = [url.split(".com")[1] for url in urls]
    return shortUrls


async def db_connection():
    db_user = getenv("POSTGRES_USER")
    db_pass = getenv("POSTGRES_PASSWORD")
    db_name = getenv("POSTGRES_DB")
    db_host = "localhost"
    
    return await asyncpg.connect(f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}")


async def insertIgIntoDB(urls):
    conn = await db_connection()
    for url in urls:
        await conn.execute("INSERT INTO urls (url) VALUES ($1) ON CONFLICT (url) DO NOTHING", url)

    await conn.close()

async def main():
    load_dotenv()
    while true:
        igUrls = scrape_ig(amount = 100)
        await insertIgIntoDB(igUrls)
        time.sleep(120)

        
if __name__ == "__main__":
    asyncio.run(main())
