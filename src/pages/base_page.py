from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def go_to(self):
        # Navigate to base_url
        self.page.goto(self.base_url)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        # Waiting for element to exist
        self.page.wait_for_selector(selector, timeout=timeout)

    def expect_visible(self, selector: str):
        # Verify that the element is visible
        expect(self.page.locator(selector)).to_be_visible()

    def expect_enabled(self, selector: str):
        # Verify that the element is enabled
        expect(self.page.locator(selector)).not_to_be_disabled()

    def expect_disabled(self, selector: str):
        # Verify that the element is disabled
        expect(self.page.locator(selector)).to_be_disabled()