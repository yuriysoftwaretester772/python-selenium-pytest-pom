import pytest
from pages.home_page import AmazonHomePage
from pages.search_result_page import AmazonSearchResultPage

@pytest.mark.parametrize("item", [
    "nike air max",
    "reebok crossfit shoes men",
    "puma sneakers",
    "adidas classic shoes"])
@pytest.mark.regressiontest
def test_search_multiple_items(browser, item):
    home_page = AmazonHomePage(browser)
    search_result_page = AmazonSearchResultPage(browser)

    # Navigate to Amazon.com home page
    home_page.load_page()

    # Verify that web page title contains Amazon.com
    home_page.verify_title()

    # Search for item
    home_page.search_item(item)

    # Verify that web page title contains the search item
    search_result_page.verify_title(item)