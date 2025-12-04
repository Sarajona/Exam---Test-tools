import re
from playwright.sync_api import expect
from behave import given, when, then
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage

@given(u'user is on the "Katalog" page')
def step_given_catalog_page(context):
    context.catalog_page = CatalogPage(context.page, context.base_url)
    context.catalog_page.go_to_page()

@then(u'user should see a list of books')
def step_then_list_of_books(context):
    #Find book list
    book_list = context.catalog_page.get_book_list()
    #Verify that book list has at least 1 book
    assert book_list.count() > 0

@then(u'every book should have a title, an author and a heart icon')
def step_then_books_have_details(context):
    book_list = context.catalog_page.get_book_list()
    count = book_list.count()
    for i in range(count):
        book = book_list.nth(i)
        #Verify that each book is visible
        expect(book).to_be_visible()

        #Verify that book has heart button
        heart_button = context.catalog_page.get_heart_button(book)
        expect(heart_button).to_be_visible()

        #Verify that title and author has correct format
        book_details = book.inner_text()
        pattern = r'❤️\s*"[^"]+",\s*.+'  # starts with heart inside citation marks, then any characters inside citation marks, comma, space, then at least one character
        if not re.match(pattern, book_details):
            raise AssertionError(f'Book #{i+1} has wrong format: "{book_details}"')

@given(u'user is on the "Lägg till bok" page')
def step_given_add_book_page(context):
    context.catalog_page = CatalogPage(context.page, context.base_url)
    context.add_book_page.go_to_page()

    #verify that title and author fields are visible
    title_field = context.add_book_page.get_title_field()
    author_field = context.add_book_page.get_author_field()
    expect(title_field).to_be_visible()
    expect(author_field).to_be_visible()

@when(u'user enters {title} and {author}')
def step_when_enter_fields(context, title, author):
    #Convert example values <empty> to empty string
    if title == "<empty>":
        title = ""
    if author == "<empty>":
        author = ""

    #Fill title and author fields
    context.add_book_page.fill_title(title)
    context.add_book_page.fill_author(author)

@when(u'clicks on the "Lägg till bok" button')
def step_then_click_add_button(context):
    #Click on "Lägg till bok" button
    context.add_book_page.click_add_button()

@then(u'the fields should be cleared')
def step_then_fields_cleared(context):
    #Find and verify that fields are cleared
    title_field = context.add_book_page.get_title_field()
    author_field = context.add_book_page.get_author_field()
    expect(title_field).to_have_value("")
    expect(author_field).to_have_value("")

@then(u'{title} by {author} should be added to catalog')
def step_then_book_added(context, title, author):
    #click on "Katalog" tab to go back to catalog tab
    context.catalog_page.go_to_page()

    #Find book and verify it has title and author in correct format
    new_book_item = context.catalog_page.get_book_item(title, author)
    expect(new_book_item).to_be_visible()

@then(u'the result should be {result}')
def step_then_result_is_correct(context, result):
    #Find button
    add_book_button = context.add_book_page.get_add_book_button()

    #If button should be enabled...
    if result == "button is enabled":
        #Expect NOT disabled
        expect(add_book_button).not_to_be_disabled()

    #If button should be disabled...
    elif result == "button is disabled":
        #Expect disabled
        expect(add_book_button).to_be_disabled()