from playwright.sync_api import Page
from .base_page import BasePage

class AddBookPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def go_to_page(self):
        # navigate to base url first
        self.go_to()
        # Find button for "Lägg till bok" tab and click
        self.page.get_by_test_id("add-book").click()

    def get_title_field(self):
        #Return title field
        return self.page.get_by_test_id('add-input-title')

    def get_author_field(self):
        #Return author field
        return self.page.get_by_test_id('add-input-author')

    def fill_title(self, title: str):
        #Fill the title input field
        self.get_title_field().fill(title)

    def fill_author(self, author: str):
        #Fill the author input field
        self.get_author_field().fill(author)

    def get_add_book_button(self):
        return self.page.get_by_test_id('add-submit')

    def click_add_button(self):
        #Click on "Lägg till bok" button
        self.get_add_book_button().click()

    def add_book(self, title: str, author: str):
        #Fill fields and click button to submit
        self.fill_title(title)
        self.fill_author(author)
        self.click_add_button()