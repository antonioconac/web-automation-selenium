from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class OrderCompletePage(BasePage):
    HEADER = (By.CLASS_NAME, "complete-header")
    MESSAGE = (By.CLASS_NAME, "complete-text")
    RETURN_BUTTON = (By.ID, "back-to-products")

    def get_order_completion_messages(self):
        return [
            self.driver.find_element(*self.HEADER).text,
            self.driver.find_element(*self.MESSAGE).text
        ]

    def return_to_homepage(self):
        self.wait.until(EC.element_to_be_clickable(self.RETURN_BUTTON)).click()