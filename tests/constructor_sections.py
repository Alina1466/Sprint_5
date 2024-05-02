from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, './/h1[@class="text text_type_main-large mb-5 mt-10"]')))

driver.find_element(By.XPATH, './/section[1]/div[1]/div[2][@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/p[@class="BurgerIngredient_ingredient__text__yp3dH"]')))

driver.find_element(By.XPATH, './/div[1][@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]')))

driver.find_element(By.XPATH, './/div[3]/span[@class="text text_type_main-default"]').click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/p[contains(text(), "Говяжий метеорит (отбивная)")]')))

driver.quit()