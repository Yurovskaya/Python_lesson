from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

# Двойное нажатие на кнопку
action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id = 'doubleClickBtn']")
action.double_click(double_click_button).perform()
print("double click button")

double_click_text = driver.find_element(By.XPATH, "//p[@id = 'doubleClickMessage']")
double_click_Message = double_click_text.text
print(double_click_Message)

text = f"{double_click_Message}"
assert double_click_Message == text
print("test good")

# Нажатие на кнопку правой кнопкой мыши
right_click = driver.find_element(By.XPATH, "//button[@id = 'rightClickBtn']")
action.context_click(right_click).perform()
print("right click button")

right_click_text = driver.find_element(By.XPATH, "//p[@id = 'rightClickMessage']")
right_click_Message = right_click_text.text
print(right_click_Message )

text = f"{right_click_Message }"
assert right_click_Message == text
print("test good")
driver.close()