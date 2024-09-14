from common_functions import add_product_to_cart, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continue_to_delivery_selection(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    login(driver,"testuser8656@example.com","TestPass123")
    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    continue_checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn--continue-checkout")))
    continue_checkout_button.click()

    delivery_address_form = wait.until(EC.presence_of_element_located((By.ID, "ekupiAddressForm")))
    assert delivery_address_form.is_displayed()
    