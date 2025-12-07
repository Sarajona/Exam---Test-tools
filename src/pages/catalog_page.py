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
        books = self.get_books()
        return books.filter(has_text=title).filter(has_text=author)

    def get_title(self, book):
        raw_title = book.inner_text().split(",")[0]
        return raw_title.strip().strip('❤️"')

    def get_author(self):
        book = self.get_books().first
        return book.inner_text().strip(' ❤️"').split(",")[1]

    def get_heart_button(self, title: str):
        # Return heart button
        test_id = f"star-{title}"
        print(f"Looking for heart button with test-id: {test_id}")
        return self.page.get_by_test_id(test_id)

    def click_heart_button(self, title: str):
        #Click on heart button
        self.get_heart_button(title).click()

    def make_favorite(self, title: str):
        if not self.is_favorite(title):
            self.click_heart_button(title)

    def remove_favorite(self, title: str):
        if self.is_favorite(title):
            self.click_heart_button(title)

    def is_favorite(self, title: str):
        #Get heart button
        heart_button = self.get_heart_button(title)
        # Check if it has a 'selected' class
        classes = heart_button.get_attribute("class")
        return "selected" in classes