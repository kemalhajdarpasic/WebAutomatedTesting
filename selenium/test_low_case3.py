from common_functions import add_product_to_cart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_remove_product_from_cart(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    remove_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "remove-from-cart")))
    remove_button.click()

    empty_cart_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".content__empty")))
    assert "Vaša košarica je prazna!" in empty_cart_element.text