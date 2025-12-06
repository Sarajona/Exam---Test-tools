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

@when(u'user hovers over a book')
def when_hover_heart_button(context):
    # get first book in catalog and hover over it
    book = context.catalog_page.get_books().first
    book.hover()
    #Get title of the book and strip away heart, whitespace and citation marks
    book_title = book.inner_text()
    book_title = book_title.strip('❤️').split(',')[0].strip().strip('"')
    #Save book to context so it can be used in then-step
    context.hovered_book = book_title

@then(u'heart button for that book becomes visible')
def then_heart_button_visible(context):
    #get heart_button using saved book title in context
    heart_button = context.catalog_page.get_heart_button(context.hovered_book)
    #Verify heart button is visible
    expect(heart_button).to_be_visible()