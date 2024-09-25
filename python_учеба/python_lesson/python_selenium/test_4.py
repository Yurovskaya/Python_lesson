import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

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
# Нажатие на клавишу Enter
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, "//select[@data-test = 'product_sort_container']")
filter.click()
print("Click filter")
time.sleep(5)
# Нажатие на стрелочку вниз
filter.send_keys(Keys.DOWN)
#  Спускаемся в самый низ выпадающего списка
# filter.send_keys(Keys.PAGE_DOWN)
time.sleep(5)
# Нажатие на стрелочку вверх
# filter.send_keys(Keys.UP)
time.sleep(5)
filter.send_keys(Keys.RETURN)
# time.sleep(5)
# # Имитация нажатия клавиш на клавиатуре
# # Нажатие на клавишу BACKSPACE
# user_mane.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_mane.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_mane.send_keys("er")
#
#
# # password = driver.find_element(By.XPATH, "//input[@id = 'password']")
# # password.send_keys(password_all_user)
# # print("Input password")
# #
# # button_login = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
# # button_login.click()
# # print("Clic login button")
