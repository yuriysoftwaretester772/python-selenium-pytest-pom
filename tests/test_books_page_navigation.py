import pytest
from pages.books_page import BooksPage


@pytest.mark.bookspageregressiontest
def test_navigate_to_books_page(browser):
    books_page = BooksPage(browser)
    books_page.navigate_to_books_page()
    books_page.verify_books_page_title()

