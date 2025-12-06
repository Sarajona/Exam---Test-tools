from .base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page, base_url: str):
        super().__init__(page, base_url)

    def get_catalog_tab_button(self):
        #Return the button for navigating to the catalog tab
        return self.page.get_by_test_id("catalog")

    def go_to_page(self):
        # Find button for "Katalog" tab
        tab_button = self.get_catalog_tab_button()
        #click if button is enabled
        if not tab_button.is_disabled():
            tab_button.click()

    def get_catalog_container(self):
        return self.page.locator('.catalog')

    def get_books(self):
        # Return all book items
        return self.page.locator('.catalog .book')

    def get_specific_book(self, title: str, author: str):
        #Return book item that contains title and author in any format
        book_list = self.get_books()
        return book_list.filter(has_text=title).filter(has_text=author)

    def get_heart_button(self, book: str):
        # Return heart button
        test_id = f"star-{book}"
        return self.page.get_by_test_id(test_id)

    def click_heart_button(self, book):
        #Click on heart button
        self.get_heart_button(book).click()

    def make_favorite(self, book: str):
        if not self.is_favorite(book):
            self.click_heart_button(book)

    def remove_favorite(self, book: str):
        if self.is_favorite(book):
            self.click_heart_button(book)

    def is_favorite(self, book: str):
        #Get heart button
        heart_button = self.get_heart_button(book)
        # Check if it has a 'selected' class
        classes = heart_button.get_attribute("class")
        return "selected" in classes