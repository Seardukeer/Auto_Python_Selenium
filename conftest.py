import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_browser():

    # initialize browser

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    yield browser
    browser.quit()

