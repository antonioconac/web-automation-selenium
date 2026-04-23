from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CartPage(BasePage):
    CONTAINER = (By.ID, "cart_contents_container")
    CONTAINER_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_items_in_cart(self):
        items = self.driver.find_elements(*self.CONTAINER_ITEM)
        return [
            [
                item.find_element(By.CLASS_NAME, "cart_quantity").text,
                item.find_element(By.CLASS_NAME, "inventory_item_name").text,
                item.find_element(By.CLASS_NAME, "inventory_item_desc").text,
                item.find_element(By.CLASS_NAME, "inventory_item_price").text,
                item.find_element(By.TAG_NAME, "button").text
            ]
            for item in items
        ]

    def remove_item_from_cart(self, button_id):
        self.wait.until(EC.presence_of_element_located((By.ID, button_id))).click()
        self.wait.until(EC.invisibility_of_element((By.ID, button_id)))

    def remove_items_from_cart(self, buttons_list):
        for button in buttons_list:
            self.remove_item_from_cart(button)

    def get_number_of_items_in_cart(self):
        return len(self.driver.find_elements(*self.CONTAINER_ITEM))

    def go_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()