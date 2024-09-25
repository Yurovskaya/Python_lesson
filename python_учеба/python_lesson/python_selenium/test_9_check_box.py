from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver: WebDriver= webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

# # Выбор чекбокса
# check_box = driver.find_element(By.XPATH, "//span[@class = 'rct-checkbox']")
# check_box.click()
# print("Click checkbox")
#
# #  Сравнение появившегося текста после выбора чекбокса
# check_box_text = driver.find_element(By.XPATH, "//div[@id= 'result']")
# value_check_box = check_box_text.text
# print(value_check_box )
#
# check_result = f"{value_check_box}"
# assert value_check_box == check_result
# print("Test GOOD")

# Выбор чекбокса
check_box_parent = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
check_box_parent.click()
print("Click checkbox parent")

check_box_child_1 = driver.find_element(By.XPATH, "(//li[contains(@class, 'rct-node')])[2]")
text_child_1 = check_box_child_1.text
print(text_child_1)

check_box_child_1_result = f"{text_child_1}"
assert text_child_1 == check_box_child_1_result
print("Text comparison GOOD")

check_box_child_2 = driver.find_element(By.XPATH, "(//li[contains(@class, 'rct-node')])[3]")
text_child_2 = check_box_child_2.text
print(text_child_2)

check_box_child_2_result = f"{text_child_2}"
assert text_child_2 == check_box_child_2_result
print("Text comparison GOOD")

check_box_child_3 = driver.find_element(By.XPATH, "(//li[contains(@class, 'rct-node')])[4]")
text_child_3 = check_box_child_3.text
print(text_child_3)

check_box_child_3_result = f"{text_child_3}"
assert text_child_3 == check_box_child_3_result
print("Text comparison GOOD")


# Выбор одного из дочерних чекбоксов
check_box_child_3 = driver.find_element(By.XPATH, "(//span[@class = 'rct-checkbox'])[4]")
check_box_child_3 .click()
print("Click checkbox child 3")

#  Сравнение появившегося текста после выбора чекбокса
check_child_3_text = driver.find_element(By.XPATH, "//div[@id= 'result']")
value_check_box_child_3 = check_child_3_text.text
print(value_check_box_child_3 )

check_result = f"{value_check_box_child_3}"
assert value_check_box_child_3 == check_result
print("Test GOOD")