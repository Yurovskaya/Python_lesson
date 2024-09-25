import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all_user = "secret_sauce"

#  Авторизация
user_mane = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_mane.send_keys(login_standard_user)
print("Input login")
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys(password_all_user)
print("Input password")
button_login = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_login.click()
print("Clic login button")
text_products = driver.find_element(By.XPATH, "//span[@class = 'title']")
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == "Products"
print("Good")
time.sleep(3)
# Выводим время
now_date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
# К имени скриншота добавляем дату и время и формат
name_screenshot = 'screenshot' + now_date + '.png'
# Создание скриншота
driver.save_screenshot('./screen/' + name_screenshot)
driver.close()
# url = "https://www.saucedemo.com/inventory.html"
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print("Good url")
# driver.close()
