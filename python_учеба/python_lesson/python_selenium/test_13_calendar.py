import calendar
import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
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

current_date_element = driver.find_element(By.XPATH, "//input[@id = 'datePickerMonthYearInput']")
current_date_element.send_keys(Keys.BACKSPACE*10)
time.sleep(5)

current_date = datetime.datetime.now()
print(current_date)

end_date = (current_date + datetime.timedelta(days=10)).strftime('%m-%d-%Y')
print(end_date)

# Ввожу полученную дату в поле
current_date_element.send_keys(end_date)
time.sleep(5)
driver.close()