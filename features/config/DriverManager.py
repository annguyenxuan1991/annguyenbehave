from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.config import EnvironmentConfig
from helpers import Helper


class DriverManager(object):
    @staticmethod
    def create_driver():
        if EnvironmentConfig.BROWSER.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument('disable-infobars')
            chrome_options.add_argument("--start-maximized")
            return webdriver.Chrome(
                chrome_options=chrome_options,
                executable_path=Helper.get_file_by_relative_path(EnvironmentConfig.RESOURCES_FOLDER_PATH))
        if EnvironmentConfig.BROWSER.lower() == "firefox":
            return webdriver.Firefox()
