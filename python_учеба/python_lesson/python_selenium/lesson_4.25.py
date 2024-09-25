from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

# Взаимодействие с мышью и передаем переменую  driver
action = ActionChains(driver)
#  Обращаемся к локатору полузунка для дальнейшего с ним взаимодействия
price = driver.find_element(By.XPATH, "//input[@id='id2']")
# Нажали на бегунок и тянем в сторону (указываем число для того чтобы потянуть вправо (тянуть в лево чило должно быь отрицательным)
# , потом отпускаем мышь и сохраняем
action.click_and_hold(price).move_by_offset(40, 0).release().perform()

print("Price +")
driver.close()
