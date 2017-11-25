from features.pom.BasePage import BasePage
from features.pom.google import Selectors as sc


class SearchPage(BasePage):
    def input_and_enter_google_search_field(self, data):
        self.input_text(sc.GOOGLE_SEARCH_AREA['GOOGLE_SEARCH_ID'], value=data, enter=True)

    def click_search_button(self):
        self.click_element(sc.GOOGLE_SEARCH_AREA['SEARCH_BUTTON_NAME'])
