from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CheckoutPage(BasePage):
    CONTAINER = (By.CLASS_NAME, "checkout_info")
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIPCODE = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONTAINER_ITEM = (By.CLASS_NAME, "cart_item")

    CHECKOUT_FIELDS = {
        "//div[@data-test='payment-info-label']": "Payment Information:",
        "//div[@data-test='payment-info-value']": "SauceCard #31337",
        "//div[@data-test='shipping-info-label']": "Shipping Information:",
        "//div[@data-test='shipping-info-value']": "Free Pony Express Delivery!",
        "//div[@data-test='total-info-label']": "Price Total",
        "//div[@data-test='subtotal-label']": "Item total: $",
        "//div[@data-test='tax-label']": "Tax: $",
        "//div[@data-test='total-label']": "Total: $"
    }

    def fill_in_details(self, firstname, lastname, zipcode):
        self.wait.until(EC.presence_of_element_located(self.FIRSTNAME))
        self.driver.find_element(*self.FIRSTNAME).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME).send_keys(lastname)
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)

    def go_to_second_step(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def get_checkout_items(self):
        items = self.driver.find_elements(*self.CONTAINER_ITEM)
        return [
            [
                item.find_element(By.CLASS_NAME, "cart_quantity").text,
                item.find_element(By.CLASS_NAME, "inventory_item_name").text,
                item.find_element(By.CLASS_NAME, "inventory_item_desc").text,
                item.find_element(By.CLASS_NAME, "inventory_item_price").text
            ]
            for item in items
        ]

    def get_field_text(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).text

    def go_to_order_completion_page(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()