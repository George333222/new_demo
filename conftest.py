# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--headless")          
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)

#     yield driver
#     driver.quit()

    
# import pytest

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     xray_marker = item.get_closest_marker("xray")
#     if xray_marker:
#         report.user_properties.append(
#             ("test_key", xray_marker.args[0])
#         )

