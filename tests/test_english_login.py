import pytest

from Support_Methods import screenshot_to_file
from selenium.common import exceptions
from Pages import base_page
from Pages import login_page

''' 
Test localisation login page on english language.
Test make asserts expected text with fact text  
'''

def test_english_login_page(chrome_browser):

            # Initialize Vaults and  Methods

    page = base_page.BasePage(chrome_browser)
    text = login_page.VaultForText
    fact_text = login_page.VaultForSelectors


    try:
           # open site from base_page.__init__

        page.open_site()

           # assert text expected with fact

        assert text.eng_language == page.attribute_text(fact_text.current_language), f'Waiting current language is' \
            f'"{text.eng_language}", but text is "{page.attribute_text(fact_text.current_language)}"'
        assert text.log_in_button == page.attribute_text(fact_text.web_log_in_button), f'Waiting text on button is ' \
            f'"{text.log_in_button}", but text is "{page.attribute_text(fact_text.web_log_in_button)}"'
        assert text.sign_up_button == page.attribute_text(fact_text.web_sign_up_button), f'Waiting text on button is ' \
            f'"{text.sign_up_button}", but text is "{page.attribute_text(fact_text.web_sign_up_button)}"'
        assert text.login_text == page.attribute_text(fact_text.web_login_text), f'Waiting text is ' \
            f'"{text.login_text}", but text is "{page.attribute_text(fact_text.web_login_text)}"'
        assert text.email_field == page.attribute_text(fact_text.web_email_field), f'Waiting text is ' \
            f'"{text.email_field}", but text is "{page.attribute_text(fact_text.web_email_field)}"'
        assert text.password_field == page.attribute_text(fact_text.web_password_field), f'Waiting text is ' \
            f'"{text.password_field}", but text is "{page.attribute_text(fact_text.web_password_field)}"'


        assert text.email_placeholder == page.get_attribute_placeholder(fact_text.web_email_placeholder), \
            f'Waiting text in placeholder is "{text.email_placeholder}", but text is ' \
            f'"{page.get_attribute_placeholder(fact_text.web_email_placeholder)}"'


        assert text.password_placeholder == page.get_attribute_placeholder(fact_text.web_password_placeholder), \
            f'Waiting text in placeholder is "{text.password_placeholder}", but text ' \
            f'is "{page.get_attribute_placeholder(fact_text.web_password_placeholder)}"'


        assert text.stay_signed == page.attribute_text(fact_text.web_stay_signed), f'Waiting text in element is ' \
            f'"{text.stay_signed}", but text is "{page.attribute_text(fact_text.web_stay_signed)}"'
        assert text.forgot_password == page.attribute_text(fact_text.web_forgot_password), f'Waiting text ' \
            f'is "{text.forgot_password}", but text is "{page.attribute_text(fact_text.web_forgot_password)}'
        assert text.submit_btn_login == page.attribute_text(fact_text.web_submit_btn_login), \
            f'Waiting text is "{text.submit_btn_login}", but text is ' \
            f'"{page.attribute_text(fact_text.web_submit_btn_login)}"'
        assert text.have_not_account == page.attribute_text(fact_text.web_have_not_account), \
            f'Waiting text is "{text.have_not_account}", but text ' \
            f'is "{page.attribute_text(fact_text.web_have_not_account)}"'
        assert text.sign_up_account == page.attribute_text(fact_text.web_sign_up_account), \
            f'Waiting text is "{text.sign_up_account}", but text ' \
            f'is "{page.attribute_text(fact_text.web_sign_up_account)}"'
        assert text.privacy_policy == page.attribute_text(fact_text.web_privacy_policy), \
            f'Waiting text is "{text.privacy_policy}", but text ' \
            f'is "{page.attribute_text(fact_text.web_privacy_policy)}"'
        assert text.rights_reserved == page.attribute_text(fact_text.web_rights_reserved), \
            f'Waiting text is "{text.rights_reserved}", but text ' \
            f'is "{page.attribute_text(fact_text.web_rights_reserved)}"'
        assert text.authorised == page.attribute_text(fact_text.web_authorised), \
            f'Waiting text is "{text.authorised}", but text is "{page.attribute_text(fact_text.web_authorised)}"'

            # Take a screenshot login page if test success

        screenshot_to_file.make_success_screenshot(chrome_browser)

    except AssertionError:
        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise AssertionError

    except exceptions.NoSuchElementException:
        screenshot_to_file.make_fail_screenshot(chrome_browser)
        raise exceptions.NoSuchElementException
