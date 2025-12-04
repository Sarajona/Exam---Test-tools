from .base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page, base_url: str):
        super().__init__(page, base_url)

    def go_to_page(self):
        # Find button for "Katalog" tab
        catalog_button = self.page.get_by_test_id("catalog")
        #click IF button is enabled
        if not catalog_button.is_disabled():
            catalog_button.click()

    def get_book_list(self):
        # Return all book items
        return self.page.locator('.catalog .book')

    def get_book_item(self, title: str, author: str):
        #Return book item that contains title and author in any format
        book_list = self.get_book_list()
        return book_list.filter(has_text=title).filter(has_text=author)

    def get_heart_button(self, book):
        # Return heart button
        return book.locator('.star')

    def catalog_tab_button(self):
        #Return the button for navigating to the catalog tab
        return self.page.get_by_test_id("catalog")