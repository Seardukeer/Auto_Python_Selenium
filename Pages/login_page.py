from selenium.webdriver.common.by import By

class VaultForText:

    eng_language = 'English'
    log_in_button = 'Log In'
    sign_up_button = 'Sign Up'
    login_text = "Login"
    email_field = "Email"
    password_field = "Password"
    email_placeholder = "Enter your email address"
    password_placeholder = "Enter your password"
    stay_signed = "Stay signed in"
    forgot_password = "Forgot password?"
    submit_btn_login = "Log In"
    have_not_account = "Don't have an account? Sign Up"
    sign_up_account = "Sign Up"
    privacy_policy = "Privacy Policy"
    rights_reserved = "Some_info_about_rights"
    authorised = "Some_info"

class VaultForSelectors:

    current_language = (By.CSS_SELECTOR, '.vs__selected-options span.vs__selected')
    web_log_in_button = (By.CSS_SELECTOR, '.header__btn.btn.btn_b-blue.btn_b-white.nuxt-link-active')
    web_sign_up_button = (By.CSS_SELECTOR, '.header__btn.btn.btn_b-blue.signup')
    web_login_text = (By.CSS_SELECTOR, 'h1.auth__title')
    web_email_field = (By.XPATH, '//*[@class="auth__label" and contains(text(), "Email")]')
    web_password_field = (By.XPATH, '//*[@class="auth__label" and contains(text(), "Password")]')
    web_email_placeholder = (By.XPATH, '//*/input[contains(@placeholder, "Enter your email address")]')
    web_password_placeholder = (By.XPATH, '//*/input[contains(@placeholder, "Enter your password")]')
    web_stay_signed = (By.CSS_SELECTOR, 'p.auth__checkbox-desc')
    web_forgot_password = (By.CSS_SELECTOR, '.auth__form__link a.auth__link')
    web_submit_btn_login = (By.CSS_SELECTOR, '.form-default__btn.btn.btn_blue')
    web_have_not_account = (By.XPATH, '//*/div[contains(text(), "Don\'t have an account")]')
    web_sign_up_account = (By.CSS_SELECTOR, '.auth__links a.auth__link')
    web_privacy_policy = (By.CSS_SELECTOR, 'footer.copyright a')
    web_rights_reserved = (By.XPATH, '//*/footer/p[contains(text(), "All rights reserved")]')
    web_authorised = (By.XPATH, '//*/footer/p[contains(text(), "authorised and regulated")]')
    coinloan_logo = (By.CSS_SELECTOR, 'a .logo-default img')
    intercom_button = (By.CSS_SELECTOR, '.intercom-lightweight-app-launcher.intercom-launcher')
    email_field = (By.CSS_SELECTOR, '#InputEmail')
    password_field = (By.CSS_SELECTOR, '#InputPassword')
    btn_login = (By.CSS_SELECTOR, '.form-default__btn.btn.btn_blue')
    field_2fa = (By.NAME, 'tfa_token')
    field_2fa_input = (By.ID, 'InputCode')
    incorrect_2fa = (By.CSS_SELECTOR, 'p.auth__msg-desc')
    alert_2fa = (By.CSS_SELECTOR, 'span.validation-msg')
