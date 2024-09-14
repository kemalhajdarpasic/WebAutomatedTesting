from common_functions import add_product_to_cart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    item_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item__list")))
    assert item_list.text.strip(), "Košarica je prazna: Nema proizvoda u košarici"

    cart_totals = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "js-cart-totals")))
    assert any(cart_totals.text.strip()), "Cijena nije ispisana"
