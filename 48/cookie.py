from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

search1 = driver.find_element(by=By.ID, value = "langSelect-DE")
search1.click()

time.sleep(3)
cookie = driver.find_element(by=By.ID, value = "bigCookie")

def clicking():
    for x in range(30):
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
    check()
u = False
def check():
    money_driver = driver.find_element(by=By.ID, value = "cookies")
    money = money_driver.text.split()[0]
    money = money.replace(",", "")
    x = 17
    time.sleep(0.3)
    while x != -1:
        value = ("productPrice" + str(x))
        try:
            product = driver.find_element(by=By.ID, value=value)
            product_finish = product.text.replace(",", "")
            try:
                if float(product_finish) <= float(money):
                    driver.find_element(by=By.ID, value=f"product{x}").click()
            except ValueError:
                pass
        except NoSuchElementException:
            pass
        x -= 1



    clicking()


clicking()

