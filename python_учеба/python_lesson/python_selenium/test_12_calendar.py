import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id = 'datePickerMonthYearInput']")
new_date.send_keys(Keys.BACKSPACE*10)
time.sleep(5)
new_date.send_keys("03/23/2024")
time.sleep(5)
new_date.send_keys(Keys.RETURN)
driver.close()
# new_date = driver.find_element(By.XPATH, "//input[@id = 'datePickerMonthYearInput']")
# new_date.click()
# time.sleep(5)
# now_date = datetime.datetime.utcnow().strftime("%d")
# print(now_date)
# date = int(now_date) + 1
# locator = driver.find_element(By.XPATH, "//div[@aria-label = 'Choose Saturday, March " + str(date) + "th, 2024']")
# print(locator)



