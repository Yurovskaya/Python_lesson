from selenium import webdriver
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
password_all_user = "secret"

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

warring_text = driver.find_element(By.XPATH, "//h3[@data-test= 'error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Good test")
driver.close()
