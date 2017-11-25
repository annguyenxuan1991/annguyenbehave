from features.config.DriverManager import DriverManager


def before_all(context):
    pass

def before_feature(context, feature):
    """
    Placeholder for any before feature hooks needed
    """
    pass


def before_scenario(context, scenario):
    init_browser_session(context)
    context.browser.get("http://google.com.vn")


def init_browser_session(context):
    context.browser = DriverManager.create_driver()

def after_scenario(context, scenario):
    pass


def after_all(context):
    """
    Placeholder for any before feature hooks needed
    """
    pass
