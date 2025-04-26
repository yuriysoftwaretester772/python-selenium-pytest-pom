from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import AmazonBasePage

class AmazonHomePage(AmazonBasePage):
    URL = 'https://www.amazon.com'
    PAGE_TITLE = 'Amazon.com'

    def load_page(self):
        self.browser.get(self.URL)
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.SEARCH_FIELD)
        )

    def verify_title(self):
        actual_title = self.browser.title
        assert self.PAGE_TITLE in actual_title, f"Expected '{self.PAGE_TITLE}' in title, but got '{actual_title}'"