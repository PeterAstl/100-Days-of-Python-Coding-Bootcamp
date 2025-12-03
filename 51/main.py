import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net")

time.sleep(3)
go = driver.find_element(by= By.CSS_SELECTOR, value = "span.start-text")
go.click()

time.sleep(30)

down = driver.find_element(By.CSS_SELECTOR, "span.download-speed")
print(down.text)

time.sleep(30)

up = driver.find_element(By.CSS_SELECTOR, "span.upload-speed")
print(up.text)


