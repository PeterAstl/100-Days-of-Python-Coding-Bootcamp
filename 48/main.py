from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

# event = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
# event_name = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget ul li a")
# events = {}
#
# for n in range(len(event)):
#     events[n] = {
#         "time": event[n].text,
#         "name": event_name[n].text
#     }
# print(events)

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Text", Keys.ENTER)

# search1 = driver.find_element(By.NAME, "fName")
# search2 = driver.find_element(By.NAME, "lName")
# search3 = driver.find_element(By.NAME, "email")
# search4 = driver.find_element(By.CSS_SELECTOR, "button")
#
# search1.send_keys("XYZ")
# search2.send_keys("ZYX")
# search3.send_keys("XZY@gmail.com")
# search4.click()

