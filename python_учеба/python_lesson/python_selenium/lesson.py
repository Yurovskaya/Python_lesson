import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# user_mane = driver.find_element_by_id("user-name")
# user_mane = driver.find_element(By.ID, "user-name") #ID
# user_mane = driver.find_element(By.NAME, "user-name")   #NAME
# user_mane = driver.find_element(By.XPATH, "//input[@id = 'user-name']")   #XPATH
user_mane = driver.find_element(By.XPATH, "//input[@data-test = 'username']")   #XPATH
user_mane.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")   #CSS_SELECTOR
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value = 'Login']")
button_login.click()


# time.sleep(5)
# driver.close()



