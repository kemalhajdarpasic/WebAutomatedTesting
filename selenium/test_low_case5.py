from common_functions import add_product_to_cart, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_enter_valid_delivery_information(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    login(driver, "testuser8656@example.com", "TestPass123")
    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    continue_checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn--continue-checkout")))
    continue_checkout_button.click()

    delivery_address_form = wait.until(EC.presence_of_element_located((By.ID, "ekupiAddressForm")))

    first_name_input = wait.until(EC.presence_of_element_located((By.ID, "address.firstName")))
    first_name_input.send_keys("John")

    last_name_input = wait.until(EC.presence_of_element_located((By.ID, "address.surname")))
    last_name_input.send_keys("Smith")

    address_input = wait.until(EC.presence_of_element_located((By.ID, "address.line1")))
    address_input.send_keys("Adress 12")

    city_input = wait.until(EC.presence_of_element_located((By.ID, "address.townCity")))
    city_input.clear()
    city_input.send_keys("mo")
    wait.until(EC.visibility_of_element_located((By.ID, "ui-id-2")))

    city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-2 li")))
    city.click()

    phone_input = wait.until(EC.presence_of_element_located((By.ID, "address.phone")))
    phone_input.send_keys("063333333")

    save_address_checkbox = wait.until(EC.presence_of_element_located((By.ID, "saveAddressInMyAddressBook")))
    save_address_checkbox.click()

    default_address_checkbox = wait.until(EC.presence_of_element_located((By.ID, "defaultAddress")))
    default_address_checkbox.click()

    address_submit_button = wait.until(EC.element_to_be_clickable((By.ID, "addressSubmit")))
    address_submit_button.click()

    delivery_form_title = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='step2' and contains(@class, 'active')]//div[@class='title']")))
    assert delivery_form_title.text == 'Način slanja'