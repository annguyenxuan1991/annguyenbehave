from features.config import EnvironmentConfig
from features.config.DriverManager import DriverManager


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    init_browser(context)


def after_scenario(context, scenario):
    context.browser.close()


def after_all(context):
    pass


def init_browser(context):
    context.browser = DriverManager.create_driver()
