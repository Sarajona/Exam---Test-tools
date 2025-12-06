from behave import given, when, then
from playwright.sync_api import expect

@given(u'user is on {start_page} page')
def given_start_page(context, start_page):
    if start_page == "Lägg till bok":
        # Navigate to "lägg till bok" page
        context.add_book_page.go_to_page()
    elif start_page == "Mina böcker":
        # Navigate to "Mina böcker" page
        context.my_books_page.go_to_page()

@when(u'user navigates to {go_to_page} page')
def when_go_to_page(context, go_to_page):
    if go_to_page == "Lägg till bok":
        #Navigate to "Lägg till bok" page
        context.add_book_page.go_to_page()
    elif go_to_page == "Mina böcker":
        #Navigate to "Mina böcker" page
        context.my_books_page.go_to_page()
    elif go_to_page == "Katalog":
        #Navigate to "Katalog" page
        context.catalog_page.go_to_page()

@then(u'{go_to_page} page is shown')
def then_result(context, go_to_page):
    if go_to_page == "Lägg till bok":
        #Find form for adding book and verify it's visible
        expect(context.add_book_page.get_form_container()).to_be_visible()
    elif go_to_page == "Mina böcker":
        #Find div that will contain favorites list and verify it's visible
        expect(context.my_books_page.get_favorites_container()).to_be_visible()
    elif go_to_page == "Katalog":
        #Find div that contains catalog and verify it's visible
        expect(context.catalog_page.get_catalog_container()).to_be_visible()