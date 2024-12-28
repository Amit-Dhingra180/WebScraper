from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Credentials
username = "username"
password = "password"

# Specify the path to chromedriver
driver_path = r"path/to/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get("https://x.com/i/flow/login?lang=en")

    # Enter username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "text"))).send_keys(username)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # Wait for password field and enter password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()

    # Wait for the home page to load
    WebDriverWait(driver, 10).until(EC.url_contains("https://x.com/home"))

    # Navigate to the trending tab
    driver.get("https://x.com/explore/tabs/trending")

    # Wait for the trending page to load and print the title
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Trending tab title:", driver.title)

    # Loop through the trending topics (1 to 5)
    for i in range(1, 6):
        xpath = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/span'
        trending_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).text
        print(trending_text)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
