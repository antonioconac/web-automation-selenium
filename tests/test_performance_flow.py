import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from pages.order_complete_page import OrderCompletePage
from variables import general_variables


@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
    ])
def test_performance_for_login(driver, username, password):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    start = time.perf_counter()
    login.login(username, password)
    inventory.wait.until(
        EC.visibility_of_element_located(
            inventory.CONTAINER
        )
    )
    end = time.perf_counter()
    time_to_run = end - start
    assert time_to_run < 1.0, "Performance too slow"

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_performance_for_complete_flow(complete_order):
    completion = OrderCompletePage(complete_order)
    assert completion.validate_element_on_page(completion.HEADER)
    assert completion.check_url("https://www.saucedemo.com/checkout-complete.html")
    assert completion.get_order_completion_messages() == [
        general_variables.COMPLETE_ORDER_HEADER,
        general_variables.COMPLETE_ORDER_TEXT
    ]
    completion.return_to_homepage()
    assert completion.check_url("https://www.saucedemo.com/inventory.html")