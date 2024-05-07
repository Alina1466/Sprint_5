from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))
        driver.find_element(By.LINK_TEXT, StellarLocators.REG).click()
        driver.find_element(By.XPATH, StellarLocators.NAME_REG).send_keys('Алина')
        driver.find_element(By.XPATH, StellarLocators.EMAIL_REG).send_keys('zuevaalina8888@yandex.ru')
        driver.find_element(By.XPATH, StellarLocators.PASS_REG).send_keys('Mi1466')
        driver.find_element(By.XPATH, StellarLocators.BUT_REG).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"


    def test_incorrect_password(self, driver):
        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))
        driver.find_element(By.LINK_TEXT, StellarLocators.REG).click()
        driver.find_element(By.XPATH, StellarLocators.NAME_REG).send_keys('Алина')
        driver.find_element(By.XPATH, StellarLocators.EMAIL_REG).send_keys('zuevaalina8888@yandex.ru')
        driver.find_element(By.XPATH, StellarLocators.PASS_REG).send_keys('Mi146')
        driver.find_element(By.XPATH, StellarLocators.BUT_REG).click()
        error_pass = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register" and error_pass.text == "Некорректный пароль"