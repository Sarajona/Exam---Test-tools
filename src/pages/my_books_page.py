from playwright.sync_api import Page
from .base_page import BasePage

class MyBooksPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def get_my_books_tab_button(self):
        #Return the button for navigating to "Mina böcker" tab
        return self.page.get_by_test_id("favorites")

    def go_to_page(self):
        # Find button for navigating to "Mina böcker" tab
        tab_button = self.get_my_books_tab_button()
        # click if button is enabled
        if not tab_button.is_disabled():
            tab_button.click()

    def get_favorites_container(self):
        return self.page.locator('.favorites')

    def get_favorites_list_locator(self):
        #Return locator for all li.book in the list of favorites
        favorites_ol = self.page.get_by_role("list")
        return favorites_ol.locator("li.book")

    def get_favorites_list_text(self):
        #Returns list with titles of all favorites as text
        items = self.get_favorites_list_locator()
        return items.all_text_contents()

    def get_favorite(self, title: str):
        #Find all favorites and filter for title
        all_favorites = self.get_favorites_list_locator()  # Locator
        favorite_item = all_favorites.filter(has_text=title)  # filtrera på text
        #return item if found, otherwise return none
        if favorite_item.count() > 0:
            return favorite_item
        return None

    def get_info_text(self):
        #Return the info text
        return self.page.get_by_role("paragraph").get_by_text("När du valt, kommer dina favoritböcker att visas här.")