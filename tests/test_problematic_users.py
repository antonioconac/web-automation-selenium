import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username,password", [("locked_out_user", "secret_sauce")])
def test_log_in_locket_out_user(login):
    login = LoginPage(login)
    error_box = login.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert error_box.text == "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.parametrize("username,password", [("locked_out_user_mock", "secret_sauce")])
def test_log_in_non_existing_user(login):
    login = LoginPage(login)
    error_box = login.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert error_box.text == "Epic sadface: Username and password do not match any user in this service"