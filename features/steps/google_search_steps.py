from behave import given, when, step, then
from features.config import EnvironmentConfig as EnvConfig
from features.pom.google.SearchPage import SearchPage
from features.pom.google.SearchResultPage import SearchResultPage

__author__ = 'An Nguyen'


@given('user navigates to Google page')
def step_navigate_to_google_page(context):
    SearchPage(context.browser).navigate(EnvConfig.BASE_URL)


@when('user inputs "{keyword}" keyword into search field')
def step_input_keyword_to_search_field(context, keyword):
    SearchPage(context.browser).input_google_search_field(keyword)


@step('user clicks Search button')
def step_click_search_button(context):
    SearchPage(context.browser).click_search_button()


@step('he is continue to clicking Gamek website in search results')
def step_click_gamek_site(context):
    SearchResultPage(context.browser).click_gamek_hyperlink()


@then('he do not want to do anything else')
def step_do_nothing(context):
    pass
