from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestConstructorSections:
    def test_constructor_sections(self, driver):
        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))
        driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("zuevaalina8888@yandex.ru")
        driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("Mi1466")
        driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))
        driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.ACCOUNT_LIST)))
        driver.find_element(By.XPATH, StellarLocators.CONSTRUCT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))

        assert expected_conditions.visibility_of_element_located((By.XPATH, StellarLocators.INPUT_ACCOUNT))


    class TestTransitionStellarburgers:
        def test_transition_stellarburgers(self, driver):
            driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))
            driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("zuevaalina8888@yandex.ru")
            driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("Mi1466")
            driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))
            driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, StellarLocators.ACCOUNT_LOGIN)))
            driver.find_element(By.XPATH, StellarLocators.LOGO).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))

            assert driver.current_url == "https://stellarburgers.nomoreparties.site/"