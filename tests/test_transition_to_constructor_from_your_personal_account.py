from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from locators import StellarLocators
from conftest import driver

class TestTransitionToConstructorFromYourPersonalAccount:
    def test_transition_to_sauces(self, driver):
        driver.find_element(*StellarLocators.SAUCES).click()
        assert ('tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' in driver.find_element(*StellarLocators.SAUCES).get_attribute('class'))

    def test_transition_to_rolls(self, driver):
        driver.find_element(*StellarLocators.SAUCES).click()
        driver.find_element(*StellarLocators.ROLLS).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*StellarLocators.ROLLS).get_attribute('class')

    def test_transition_to_filling(self, driver):
        driver.find_element(*StellarLocators.FILLINGS).click()
        assert ('tab_tab_type_current__2BEPc' in driver.find_element(*StellarLocators.FILLINGS)
                .get_attribute('class'))