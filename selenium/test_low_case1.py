from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    supermarket_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/bs/c/10011']")))
    supermarket_button.click()

    assert "Supermarket" in driver.title

    product_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

    selected_product = product_items[0]

    product_image = selected_product.find_element(By.CLASS_NAME, "thumb")
    product_image.click()

    increase_quantity_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-qty-selector-plus")))
    increase_quantity_button.click()

    input_quantity = driver.find_element(By.ID, "pdpAddtoCartInput")
    assert input_quantity.get_attribute("value") == "2"

    add_to_card_button = driver.find_element(By.ID, "addToCartButton")
    add_to_card_button.click()

    mini_cart_price = driver.find_element(By.CLASS_NAME, "mini-cart-price").text

    assert mini_cart_price != "0,00 KM"
