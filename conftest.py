from selenium import webdriver
import pytest
from URLs import URL

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL.main)
    yield driver
    driver.quit()