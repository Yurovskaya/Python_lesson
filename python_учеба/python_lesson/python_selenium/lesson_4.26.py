import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# импортирование класса Select, для работы с дроп-даунами
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()
#
# login_standard_user = "standard_user"
# password_all_user = "secret_sauce"
#
# #  Авторизация
# user_mane = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
# user_mane.send_keys(login_standard_user)
# print("Input login")
# password = driver.find_element(By.XPATH, "//input[@id = 'password']")
# password.send_keys(password_all_user)
# print("Input password")
# button_login = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
# button_login.click()
# print("Clic login button")
#  Взаимодействие с Drop Down
# select = Select(driver.find_element(By.XPATH, "//select[@class = 'product_sort_container']"))
# time.sleep(5)
# #  Взаимодействие с библиотекой Select без открытия  Drop Down
# #  Взаимодействие с библиотекой Select без открытия  ищем по тексту
# # select.select_by_visible_text('Name (Z to A)')
# #  Взаимодействие с библиотекой Select без открытия  ищем по value
# select.select_by_value('za')

base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.maximize_window()

#  Взаимодействие с Drop Down
#  Нажимаю на поле для открытия Drop Down (выбор страны из выпадающего списка)
click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby= 'select2-country-container']")
click_drop.click()
time.sleep(5)
#  Нажимаю на поле для открытия Drop Down (выбор страны из выпадающего списка)
# click_country = driver.find_element(By.XPATH, "(//li[@class= 'select2-results__option'])[1]")
# click_country.click()
#  Ввод названия нужного значения для выбора в поле и нажатие на кнопку Enter
input_country = driver.find_element(By.XPATH, "(//input[@class= 'select2-search__field'])[2]")
input_country.send_keys('Japan')
time.sleep(3)
input_country.send_keys(Keys.ENTER)
