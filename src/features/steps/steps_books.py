import re
from playwright.sync_api import expect
from behave import given, when, then

@given(u'user is on the "Katalog" page')
def given_catalog_page(context):
    #Navigate to "Katalog" page
    context.catalog_page.go_to_page()

@then(u'user should see a list of books')
def then_list_of_books(context):
    #Find book elements
    books = context.catalog_page.get_books()
    # Look at first book element and verify that it is visible
    expect(books.first).to_be_visible()
    #Verify that book list has at least 1 book
    assert books.count() > 0

@then(u'every book should have a title, an author and a heart icon')
def then_books_have_details(context):
    books = context.catalog_page.get_books()
    count = books.count()
    for i in range(count):
        book = books.nth(i)
        #Verify that each book is visible
        expect(book).to_be_visible()
        #Verify that there is a heart button, title and author in correct format
        book_details = book.inner_text()
        pattern = r'❤️\s*"[^"]+",\s*.+'  # starts with heart, then any characters inside citation marks, comma, space, then at least one character
        if not re.match(pattern, book_details):
            raise AssertionError(f'Book #{i+1} has wrong format: "{book_details}"')

@given(u'user is on the "Lägg till bok" page')
def given_add_book_page(context):
    #Navigate to "Lägg till bok" page
    context.add_book_page.go_to_page()
    #verify that title and author fields are visible
    title_field = context.add_book_page.get_title_field()
    author_field = context.add_book_page.get_author_field()
    expect(title_field).to_be_visible()
    expect(author_field).to_be_visible()

@when(u'user adds {title} by {author}')
def when_add_book(context, title, author):
    if title == "space" and author == "space":
        # exchange string to just one space
        title = " "
        author = " "
        context.add_book_page.add_book(title, author)
    else: context.add_book_page.add_book(title, author)

@when(u'clicks on the "Lägg till bok" button')
def then_click_add_button(context):
    #Click on "Lägg till bok" button
    context.add_book_page.click_add_button()

@then(u'the fields should be cleared')
def then_fields_cleared(context):
    #Find and verify that fields are cleared
    title_field = context.add_book_page.get_title_field()
    author_field = context.add_book_page.get_author_field()
    expect(title_field).to_have_value("")
    expect(author_field).to_have_value("")

@then(u'{title} by {author} should be added to catalog')
def then_book_added(context, title, author):
    #click on "Katalog" tab to go back to catalog tab
    context.catalog_page.go_to_page()
    #Divert edge case example to a stricter locator
    if title == "space" and author == "space":
        #exchange string to just one space
        title = " "
        author = " "
        # Find all books
        books = context.catalog_page.get_books()
        # Verify that new book exists in catalog
        books.get_by_text(f'{title}, {author}', exact=True)
    #Verify that new book exists in catalog
    else:
        new_book_item = context.catalog_page.get_specific_book(title, author)
        expect(new_book_item).to_be_visible()

@when(u'user enters {title} and {author}')
def when_enter_fields(context, title, author):
    #Convert example values <empty> to empty string
    if title == "<empty>":
        title = ""
    if author == "<empty>":
        author = ""
    #Fill title and author fields
    context.add_book_page.fill_title(title)
    context.add_book_page.fill_author(author)

@then(u'the result should be {result}')
def then_result_is_correct(context, result):
    #Find button
    add_book_button = context.add_book_page.get_add_book_button()
    if result == "button is enabled":
        #Verify button is NOT disabled
        expect(add_book_button).not_to_be_disabled()
    elif result == "button is disabled":
        #verify button IS disabled
        expect(add_book_button).to_be_disabled()

@then(u'The catalog should contain 2 copies of {title} by {author}')
def then_two_copies(context, title, author):
    # click on "Katalog" tab to go back to catalog tab
    context.catalog_page.go_to_page()
    #Find book element that has given title and author
    copies = context.catalog_page.get_specific_book(title, author).all()
    copy_count = len(copies)
    assert copy_count == 2