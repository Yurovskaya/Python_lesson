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

"""Info product #1"""

product_1 = driver.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select product 1")

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter cart")

"""Info cart product # 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1 )
assert value_product_1 == cart_value_product_1
print("Info cart product # 1 GOOD")

card_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
card_value_price_product_1 = card_price_product_1.text
print(card_value_price_product_1)
assert value_price_product_1 == card_value_price_product_1
print("Info cart price product # 1 GOOD")

checkout = driver.find_element(By.XPATH, "//button[@id = 'checkout']")
checkout.click()
print("Click button checkout")

"""Select User info"""

first_name = driver.find_element(By.XPATH, "//input[@id = 'first-name']")
first_name.send_keys("Alex")
print("Input first name ")

last_name = driver.find_element(By.XPATH, "//input[@id = 'last-name']")
last_name.send_keys("Ivanov")
print("Input last name ")

zip = driver.find_element(By.XPATH, "//input[@id = 'postal-code']")
zip.send_keys("1234")
print("Input zip")

button_continue = driver.find_element(By.XPATH, "//input[@id = 'continue']")
button_continue.click()
print("Click continue")

"""Finish cart product # 1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")
finish_value_product_1 = finish_product_1.text
print(finish_value_product_1 )
assert value_product_1 == finish_value_product_1
print("Info finish cart product # 1 GOOD")

finish_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
finish_value_price_product_1 = finish_price_product_1.text
print(finish_value_price_product_1)
assert value_price_product_1 == finish_value_price_product_1
print("Info finish cart price product # 1 GOOD")

summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = f"Item total: {finish_value_price_product_1}"
assert value_summary_price == item_total
print("Total summary price GOOD")