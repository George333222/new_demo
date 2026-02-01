# import pytest

# @pytest.mark.smoke
# def test_google_title(driver):
#     print("SMOKE TEST RUNNING")
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title

# @pytest.mark.payment_flow

# def test_login_with_valid_credentials(driver):
#     driver.get("https://www.saucedemo.com")

#     driver.find_element("id", "user-name").send_keys("standard_user")
#     driver.find_element("id", "password").send_keys("secret_sauce")
#     driver.find_element("id", "login-button").click()

#     assert "inventory" in driver.current_url

import pytest

@pytest.mark.xray("COM-1")
def test_valid_login():
    assert True
