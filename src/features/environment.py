from playwright.sync_api import sync_playwright
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.my_books_page import MyBooksPage

def before_all(context):
    #Start Playwright and browser
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)

    #Base URL
    context.base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def before_scenario(context, scenario):
    #New page for every scenario
    context.page = context.browser.new_page()

    # Navigate to base URL
    context.page.goto(context.base_url)

    # Initialize page objects
    context.catalog_page = CatalogPage(context.page, context.base_url)
    context.add_book_page = AddBookPage(context.page, context.base_url)
    context.my_books_page = MyBooksPage(context.page, context.base_url)

    # Timeout 5 seconds
    #context.page.set_default_timeout(5000)

def after_scenario(context, scenario):
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()