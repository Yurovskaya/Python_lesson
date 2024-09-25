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

menu = driver.find_element(By.XPATH, "//button[@id = 'react-burger-menu-btn']")
menu.click()
print("Clic memu button")
time.sleep(5)
link_about = driver.find_element(By.XPATH, "//a[@id = 'about_sidebar_link']")
link_about.click()
print("Clic link button")

# Нажатие на стрелку назад в браузере
driver.back()
print("go back")
time.sleep(10)

# Нажатие на стрелку вперед в браузере
driver.forward()
print("go forward")
time.sleep(10)
