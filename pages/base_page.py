from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class AmazonBasePage:
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")

    def __init__(self, browser):
        self.browser = browser

    def search_item(self, item):
        try:
            search_input = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.SEARCH_FIELD)
            )
            search_input.send_keys(item + Keys.RETURN)
        except Exception as e:
            logger.error(f"Failed to search for '{item}': {e}")
            raise