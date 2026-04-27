import pytest
from variables import general_variables, variables_complete_flow
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver, username, password):
    login = LoginPage(driver)
    login.login(username, password)
    return driver

@pytest.fixture
def cart_with_items(login):
    driver = login
    inventory = InventoryPage(driver)
    for button_to_add in list(general_variables.ITEMS_TO_ADD_IN_CART.keys())[:2]:
        inventory.add_to_cart(button_to_add)
    inventory.go_to_cart()
    return driver

@pytest.fixture
def checkout_step_one(cart_with_items):
    driver = cart_with_items
    cart = CartPage(driver)
    cart.go_to_checkout()
    return driver

@pytest.fixture
def checkout_step_two(checkout_step_one):
    driver = checkout_step_one
    checkout = CheckoutPage(driver)
    checkout.fill_in_details(
        variables_complete_flow.order_first_name,
        variables_complete_flow.order_last_name,
        variables_complete_flow.order_postal_code
    )
    checkout.go_to_second_step()
    return driver

@pytest.fixture
def complete_order(checkout_step_two):
    driver = checkout_step_two
    checkout = CheckoutPage(driver)
    checkout.go_to_order_completion_page()
    return driver