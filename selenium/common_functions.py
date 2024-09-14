from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_product_to_cart(driver):
    wait = WebDriverWait(driver, timeout=60)

    supermarket_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/bs/c/10011']")))
    supermarket_button.click()

    product_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

    selected_product = product_items[0]

    product_image = selected_product.find_element(By.CLASS_NAME, "thumb")
    product_image.click()

    increase_quantity_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-qty-selector-plus")))
    increase_quantity_button.click()

    add_to_card_button = wait.until(EC.element_to_be_clickable((By.ID, "addToCartButton")))
    add_to_card_button.click()

def login(driver, email, password):
    wait = WebDriverWait(driver, timeout=60)

    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login_link'][@href='/bs/login']")))
    login_link.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "j_username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "j_password")))

    email_input.send_keys(email)
    password_input.send_keys(password)

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()