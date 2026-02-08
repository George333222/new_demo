# File: test_sample.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.smoke
def test_google_search_title():
    """Smoke test: open Google and check title."""
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

@pytest.mark.regression
def test_bing_search_title():
    """Regression test: open Bing and check title."""
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bing.com")
    assert "Bing" in driver.title
    driver.quit()
