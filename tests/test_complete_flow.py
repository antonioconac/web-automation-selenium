import pytest
from variables import general_variables
from scripts.general_scripts import sort_prices
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_complete_page import OrderCompletePage

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_cart(cart_with_items):
    cart = CartPage(cart_with_items)
    assert cart.get_number_of_items_in_cart() == 2
    assert cart.check_url("https://www.saucedemo.com/cart.html")

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_checkout_step_one(checkout_step_one):
    checkout = CheckoutPage(checkout_step_one)
    assert checkout.check_url("https://www.saucedemo.com/checkout-step-one.html")
    assert checkout.validate_element_on_page(checkout.CONTAINER)
    assert checkout.get_element_text(checkout.CANCEL_BUTTON) == general_variables.CANCEL_BUTTON_TEXT

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_checkout_step_two(checkout_step_two):
    checkout = CheckoutPage(checkout_step_two)
    assert checkout.check_url("https://www.saucedemo.com/checkout-step-two.html")
    assert sorted(checkout.get_checkout_items()) == sorted(general_variables.CHECKOUT_PRODUCTS)
    for xpath, reference_value in checkout.CHECKOUT_FIELDS.items():
        assert reference_value in checkout.get_field_text(xpath)

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_complete_order_flow(complete_order):
    completion = OrderCompletePage(complete_order)
    assert completion.validate_element_on_page(completion.HEADER)
    assert completion.check_url("https://www.saucedemo.com/checkout-complete.html")
    assert completion.get_order_completion_messages() == [
        general_variables.COMPLETE_ORDER_HEADER,
        general_variables.COMPLETE_ORDER_TEXT
    ]
    completion.return_to_homepage()
    assert completion.check_url("https://www.saucedemo.com/inventory.html")

