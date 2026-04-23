from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    HAMBURGER_MENU_LIST = (By.CLASS_NAME, "bm-item-list")
    CLOSE_HAMBURGER_MENU = (By.ID, "react-burger-cross-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def validate_element_on_page(self, page_container):
        return self.wait.until(EC.presence_of_element_located(page_container))

    def get_element_text(self, element_id):
        return self.wait.until(EC.presence_of_element_located(element_id)).text

    def get_element_attribute(self, element, attribute):
        return self.driver.find_element(*element).get_attribute(attribute)

    def return_hamburger_menu_fields(self):
        self.wait.until(EC.presence_of_element_located(self.HAMBURGER_MENU)).click()
        self.wait.until(EC.visibility_of_element_located(self.HAMBURGER_MENU_LIST))
        hamburger_list = self.driver.find_element(*self.HAMBURGER_MENU_LIST).text
        self.wait.until(EC.presence_of_element_located(self.CLOSE_HAMBURGER_MENU)).click()
        return hamburger_list

    def logout(self):
        self.wait.until(EC.presence_of_element_located(self.HAMBURGER_MENU)).click()
        self.wait.until(EC.visibility_of_element_located(self.HAMBURGER_MENU_LIST))
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()


