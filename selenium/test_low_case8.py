from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_field(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    search_input = wait.until(EC.presence_of_element_located((By.ID, "js-site-search-input")))
    search_input.clear()
    search_input.send_keys("računar")

    search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js_search_button")))
    search_button.click()

    active_category = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='active' and text()='računar']")))
    assert active_category is not None