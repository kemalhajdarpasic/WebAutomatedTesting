from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_tire_form_submission(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    tires_link = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='yCmsComponent nav__link js_nav__link']/a[@title='Gume']")))
    tires_link.click()

    brand_select = wait.until(EC.element_to_be_clickable((By.ID, "brand")))
    brand_dropdown = Select(brand_select)
    brand_dropdown.select_by_index(1)

    season_select = wait.until(EC.element_to_be_clickable((By.ID, "SezonaGuma")))
    season_dropdown = Select(season_select)
    season_dropdown.select_by_index(1)

    diameter_select = wait.until(EC.element_to_be_clickable((By.ID, "PromjerGume")))
    diameter_dropdown = Select(diameter_select)
    diameter_dropdown.select_by_index(1)

    width_select = wait.until(EC.element_to_be_clickable((By.ID, "SirinaGume")))
    width_dropdown = Select(width_select)
    width_dropdown.select_by_index(1)

    height_select = wait.until(EC.element_to_be_clickable((By.ID, "VisinaGume")))
    height_dropdown = Select(height_select)
    height_dropdown.select_by_index(1)

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='col-sm-4']//button[@class='btn btn-default'])[1]")))
    submit_button.click()

    active_category = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='active' and text()='Auto gume']")))
    assert active_category is not None