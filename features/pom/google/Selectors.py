from selenium.webdriver.common.by import By

GOOGLE_SEARCH_AREA = {
    'GOOGLE_SEARCH_ID': (By.ID, 'lst-ib'),
    'SEARCH_BUTTON_NAME': (By.NAME, 'btnK'),
    'FEELING_LUCKY_BUTTON_NAME': (By.NAME, 'btnI')
}

SEARCH_RESULT_AREA = {
    'GAMEK_XPATH': (By.XPATH, './/a[contains(text(),"GameK:")]')
}
