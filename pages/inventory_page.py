from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class InventoryPage(BasePage):
    CONTAINER = (By.CLASS_NAME, "inventory_container")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.ID, "shopping_cart_container")
    CONTAINER_ITEM = (By.CLASS_NAME, "inventory_item")

    def get_products(self):
        items = self.driver.find_elements(*self.CONTAINER_ITEM)
        return [
            [
                item.find_element(By.CLASS_NAME, "inventory_item_name").text,
                item.find_element(By.CLASS_NAME, "inventory_item_desc").text,
                item.find_element(By.CLASS_NAME, "inventory_item_price").text,
                item.find_element(By.TAG_NAME, "button").text
            ]
            for item in items
        ]

    def sort_by(self, option):
        dropdown = Select(self.wait.until(EC.presence_of_element_located(self.SORT_SELECT)))
        dropdown.select_by_value(option)

    def add_to_cart(self, item_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    def check_item_can_be_removed(self, item_id):
        self.wait.until(EC.presence_of_element_located((By.ID, item_id)))
        return self.driver.find_element(By.ID, item_id).text

    def get_sorted_names(self):
        return [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
                for item in self.driver.find_elements(*self.CONTAINER_ITEM)
        ]

    def get_sorted_prices(self):
        return [
            item.find_element(By.CLASS_NAME, "inventory_item_price").text
                for item in self.driver.find_elements(*self.CONTAINER_ITEM)
        ]

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BADGE)).click()

    def cart_count(self):
        return int(self.driver.find_element(*self.CART_BADGE).text)