from common_functions import add_product_to_cart, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_save_cart(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    login(driver, "testuser8656@example.com", "TestPass123")
    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    save_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-save-cart-link")))
    save_cart_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "saveCartForm")))

    save_cart_name_field = wait.until(EC.presence_of_element_located((By.ID, "saveCartName")))
    save_cart_name_field.clear()
    save_cart_name_field.send_keys("Košarica 1")

    save_cart_description_field = wait.until(EC.presence_of_element_located((By.ID, "saveCartDescription")))
    save_cart_description_field.clear()
    save_cart_description_field.send_keys("Neki opis")

    save_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "saveCartButton")))
    save_cart_button.click()

    alert = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-info")))
    assert alert