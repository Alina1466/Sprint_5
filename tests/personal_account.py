from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))

driver.find_element(By.XPATH, './/input[@name="name"]').send_keys("zuevaalina8888@yandex.ru")
driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys("Mi1466")
driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

driver.quit()