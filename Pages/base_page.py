from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys

class BasePage:

    def __init__(self, driver):
        self.browser = driver
        self.base_url = "site_addres"
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def open_site(self):
        return self.browser.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    def visible_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(ec.visibility_of_element_located(locator),
                                                       message=f"Element isn't visible by locator {locator}")

    def element_attribute(self, locator, time=10):
        return self.browser.get_attribute(locator,time).until(ec.visibility_of_element_located(locator),
                                            message=f"Can't find element attribute by locator {locator}")

    def text(self, locator, time=10):
        return self.find_element(locator, time).text

    def click(self, locator):
        return self.find_element(locator).click()

    def get_attribute_placeholder(self, locator):
        attribute_point = self.find_element(locator)
        return attribute_point.get_attribute('placeholder')

    def clear_field(self, locator):
        field = self.find_element(locator)
        field.clear()
        return field

    def alt_clear_field(self, locator):
        field = self.find_element(locator)
        field.send_keys([Keys.BACKSPACE] * 1000)
        return field

    def fill_field(self, locator, *value):
        field = self.find_element(locator)
        field.click()
        field.send_keys(value)
        return field
