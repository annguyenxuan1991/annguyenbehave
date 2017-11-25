from features.pom.BasePage import BasePage
from features.pom.google import Selectors as sc


class SearchResultPage(BasePage):
    def click_gamek_hyperlink(self):
        self.click_element(sc.SEARCH_RESULT_AREA['GAMEK_XPATH'])
