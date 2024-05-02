from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')))

driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/input[@name="name"]')))

driver.find_element(By.XPATH, './/input[@name="name"]').send_keys("zuevaalina8888@yandex.ru")
driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys("Mi1466")
driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

driver.find_element(By.XPATH, './/header/nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/nav/ul/li[1]/a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))

driver.find_element(By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]').click()

driver.quit()