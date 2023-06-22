import pyotp
import pytest

from selenium.common import exceptions

from Support_Methods import screenshot_to_file
from Pages import login_page
from Pages import base_page
from Pages import main_page


''' 
Test login form with incorrect 2fa.
Test login form without 2fa.
Test login form with correct 2fa. 
'''

def test_login_correct_credentials_incorrect_2fa(chrome_browser):

    """Test login form with incorrect 2fa"""

    page = base_page.BasePage(chrome_browser)
    locators = login_page.VaultForSelectors
    page.open_site()

    try:

            # fill login form. In params locator, value

        page.fill_field(locators.email_field, "some_email")
        page.fill_field(locators.password_field, 'some_password')
        page.click(locators.btn_login)

            # fill 2fa form fields

        page.fill_field(locators.field_2fa, '123456')
        page.visible_element(locators.incorrect_2fa)
        page.alt_clear_field(locators.field_2fa)
        page.fill_field(locators.field_2fa, 'test 1')
        page.visible_element(locators.alert_2fa)
        page.alt_clear_field(locators.field_2fa)
        page.fill_field(locators.field_2fa, '1t2e3s4t')
        page.visible_element(locators.alert_2fa)

            # make success screenshot from helper method
        screenshot_to_file.make_success_screenshot(chrome_browser)

    except exceptions.TimeoutException:

            # if TimeoutException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.TimeoutException


    except exceptions.NoSuchElementException:

            # if NoSuchElementException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.NoSuchElementException


def test_login_correct_credentials_without_2fa(chrome_browser):

    """Test login form without 2fa"""

    page = base_page.BasePage(chrome_browser)
    locators = login_page.VaultForSelectors
    main_locators = main_page.MainPageLocators
    page.open_site()
    
    try:
            # fill login form elements

        page.fill_field(locators.email_field, "some_email")
        page.fill_field(locators.password_field, 'some_password')
        page.click(locators.btn_login)

            # waiting for main page

        page.visible_element(main_locators.main_page)

            # make success screenshot from helper method
        screenshot_to_file.make_success_screenshot(chrome_browser)


    except exceptions.NoSuchElementException:

            # if NoSuchElementException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.NoSuchElementException

    except exceptions.TimeoutException:

            # if TimeoutException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.TimeoutException

def test_login_with_correct_2fa(chrome_browser):

    """Test login form with incorrect 2fa"""

    page = base_page.BasePage(chrome_browser)
    locators = login_page.VaultForSelectors
    main_locators = main_page.MainPageLocators
    page.open_site()
    
    try:

            # fill login form elements

        page.fill_field(locators.email_field, "some_email")
        page.fill_field(locators.password_field, 'some_password')
        page.click(locators.btn_login)

        totp = pyotp.TOTP("secret_2fa_code")
        page.fill_field(locators.field_2fa_input, totp.now())

            # waiting for main page

        page.visible_element(main_locators.main_page)

            # make success screenshot from helper method
        screenshot_to_file.make_success_screenshot(chrome_browser)

    except exceptions.NoSuchElementException:

            # if NoSuchElementException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.NoSuchElementException

    except exceptions.TimeoutException:

            # if TimeoutException, make failed screenshot and raise exception

        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.TimeoutException
