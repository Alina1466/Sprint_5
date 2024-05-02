from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")
WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))
driver.find_element(By.XPATH, './/div/div/p[1]/a[@class="Auth_link__1fOlj"]').click()

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))
driver.find_element(By.XPATH, './/input[@name="name"]').send_keys("Алина")
driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]').send_keys(f"zuevaalina{randint(1,100000)}@yandex.ru")

driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(f"{randint(10000,99999)}")
driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, './/fieldset[3]/div/p[@class="input__error text_type_main-default"]')))
driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(f"{randint(100000,999999)}")
driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')))

driver.quit()