import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    #setup
    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    #teardown
    driver.quit()