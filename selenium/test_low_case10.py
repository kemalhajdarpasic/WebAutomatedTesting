from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_filtering(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    supermarket_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/bs/c/10011']")))
    supermarket_button.click()

    price_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '0 - 49,99 KM')]")))
    price_checkbox.click()

    dostupno_odmah_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Dostupno odmah')]")))
    dostupno_odmah_checkbox.click()

    #Provjera da li su filteri aktivni
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), '0 - 49,99 KM')]")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),  'Dostupno odmah')]")))