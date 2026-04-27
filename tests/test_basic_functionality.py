import pytest
from variables import general_variables
from scripts.general_scripts import sort_prices
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_complete_page import OrderCompletePage

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_products_on_page(login):
    inventory = InventoryPage(login)
    assert inventory.validate_element_on_page(inventory.CONTAINER)
    assert inventory.check_url("https://www.saucedemo.com/inventory.html")
    assert sorted(inventory.get_products()) == sorted(general_variables.PRODUCTS_FIELDS)

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_products_sorted(login):
    inventory = InventoryPage(login)

    name_list = [prod[0] for prod in general_variables.PRODUCTS_FIELDS]
    price_list = [prod[2] for prod in general_variables.PRODUCTS_FIELDS]
    for option in ["az", "za", "lohi", "hilo"]:
        inventory.sort_by(option)
        if option == 'az' or option == 'za':
            storing_list = inventory.get_sorted_names()
            assert storing_list == (sorted(name_list) if option == 'az' else sorted(name_list, reverse=True))
        else:
            storing_list = inventory.get_sorted_prices()
            assert storing_list == (sorted(price_list, key=sort_prices) if option == 'lohi' else sorted(price_list, key=sort_prices, reverse=True))

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_products_added_to_cart(login):
    inventory = InventoryPage(login)
    for button_to_add, button_to_remove in general_variables.ITEMS_TO_ADD_IN_CART.items():
        inventory.add_to_cart(button_to_add)
        remove_button_text = inventory.check_item_can_be_removed(button_to_remove)
        assert remove_button_text == general_variables.REMOVE_BUTTON_TEXT
    assert inventory.cart_count() == 3
    inventory.go_to_cart()
    cart = CartPage(login)
    assert cart.validate_element_on_page(cart.CONTAINER)
    assert cart.check_url("https://www.saucedemo.com/cart.html")
    cart.remove_item_from_cart("remove-sauce-labs-bolt-t-shirt")
    items_in_cart = cart.get_number_of_items_in_cart()
    assert items_in_cart == 2
    assert sorted(cart.get_items_in_cart()) == sorted(general_variables.CART_PRODUCTS)

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_hamburger_menu_and_logout(login):
    base = InventoryPage(login)
    assert base.return_hamburger_menu_fields() == general_variables.HAMBURGER_MENU_VALUES
    base.logout()
    assert base.check_url("https://www.saucedemo.com/")