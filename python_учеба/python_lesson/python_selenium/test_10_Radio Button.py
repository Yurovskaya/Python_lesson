from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# Выбор радиобаттона
radio_button = driver.find_element(By.XPATH, "(//label[@class = 'custom-control-label'])[1]")
radio_button .click()
print("Click radio button")

#  Сравнение появившегося текста после выбора радиобаттона
radio_button_text = driver.find_element(By.XPATH, "//p[@class= 'mt-3']")
value_radio_button = radio_button_text.text
print(value_radio_button)

check_result = f"{value_radio_button}"
assert value_radio_button == check_result
print("Test GOOD")