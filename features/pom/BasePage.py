from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from features.config import EnvironmentConfig as EnvSetup
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def navigate(self, url):
        self.driver.get(url)

    def click_back_button(self):
        # self.driver.navigation().back()
        self.driver.execute_script('window.history.back()')

    def click_element(self, tuple_selector, move_to_element=False,
                      timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS, by_script=False):
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
        if by_script:
            self.driver.execute_script("arguments[0].click();", element)
            self.driver.execute_script("return arguments[0].style", element)
        else:
            element.click()

    def type_text(self, tuple_selector, value=None, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        if value:
            element.send_keys(value)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    def move_to_element(self, tuple_selector):
        wait = WebDriverWait(self.driver, EnvSetup.SELENIUM_TIMEOUT_SECONDS)
        element = wait.until(EC.presence_of_element_located(tuple_selector))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))
