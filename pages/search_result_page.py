from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import AmazonBasePage

class AmazonSearchResultPage(AmazonBasePage):
    PAGE_TITLE = 'Amazon.com : '

    def verify_title(self, item):
        WebDriverWait(self.browser, 10).until(
            EC.title_contains("Amazon.com")
        )
        actual_title = self.browser.title
        assert item.lower() in actual_title.lower(), f"Expected '{item}' in title, but got '{actual_title}'"