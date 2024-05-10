from locators import StellarLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestPersonalAccount:
    def test_personal_account(self, driver):
        driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))
        driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("zuevaalina8888@yandex.ru")
        driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("Mi1466")
        driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"