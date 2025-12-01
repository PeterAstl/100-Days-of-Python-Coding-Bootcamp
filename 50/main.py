import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://account.gotinder.com/")

wait = WebDriverWait(driver, 10)

time.sleep(3)
login = driver.find_element(by = By.CSS_SELECTOR, value = 'iframe[title="Schaltfläche „Über Google anmelden“')
login.click()

"""Not Possible anymore"""