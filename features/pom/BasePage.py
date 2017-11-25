from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from features.config import EnvironmentConfig as env
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def click_element(self, selector, move_to_element=False, timeout=env.WAIT_TIMEOUT_IN_SECONDS, use_javascript=False):
        if move_to_element:
            self.move_to_element(selector)
        element = self.wait_for_element_to_be_clickable(selector, timeout)
        if use_javascript:
            self.browser.execute_script("arguments[0].click();", element)
            self.browser.execute_script("return arguments[0].style", element)
        else:
            element.click()

    def input_text(self, selector, data=False, tab=False, enter=False):
        element = self.wait_for_visibility_of_element(selector)
        if data:
            element.send_keys(data)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    def move_to_element(self, selector):
        wait = WebDriverWait(self.browser, env.WAIT_TIMEOUT_IN_SECONDS)
        element = wait.until(ec.presence_of_element_located(selector))
        ActionChains(self.browser).move_to_element(element).perform()

    def wait_for_element_to_be_clickable(self, selector, timeout=env.WAIT_TIMEOUT_IN_SECONDS):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(ec.element_to_be_clickable(selector))

    def wait_for_visibility_of_element(self, selector, timeout=env.WAIT_TIMEOUT_IN_SECONDS):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(ec.visibility_of_element_located(selector))
