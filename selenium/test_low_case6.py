from common_functions import add_product_to_cart, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_submit_form_without_required_information(driver):
    wait = WebDriverWait(driver, timeout=60)

    driver.get("https://www.ekupi.ba")
    driver.maximize_window()

    login(driver, "testuser8656@example.com", "TestPass123")
    add_product_to_cart(driver)

    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row desktop__nav']//a[@class='mini-cart-link js-mini-cart-link-items']")))
    cart_link.click()

    continue_checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn--continue-checkout")))
    continue_checkout_button.click()

    first_name_input = wait.until(EC.presence_of_element_located((By.ID, "address.firstName")))
    first_name_input.clear()

    last_name_input = wait.until(EC.presence_of_element_located((By.ID, "address.surname")))
    last_name_input.clear()

    address_input = wait.until(EC.presence_of_element_located((By.ID, "address.line1")))
    address_input.clear()

    city_input = wait.until(EC.presence_of_element_located((By.ID, "address.townCity")))
    city_input.clear()

    phone_input = wait.until(EC.presence_of_element_located((By.ID, "address.phone")))
    phone_input.clear()

    save_address_checkbox = driver.find_element(By.ID, "saveAddressInMyAddressBook")
    if save_address_checkbox.is_selected():
        save_address_checkbox.click()

    default_address_checkbox = driver.find_element(By.ID, "defaultAddress")
    if default_address_checkbox.is_selected():
        default_address_checkbox.click()

    address_submit_button = wait.until(EC.element_to_be_clickable((By.ID, "addressSubmit")))
    address_submit_button.click()

    error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]")))
    
    assert error_message.is_displayed()