from behave import given, when, then
from playwright.sync_api import expect

@given(u'{title} is not favorite')
def given_is_not_favorite(context, title):
    #Verify that book is NOT favorite
    assert not context.catalog_page.is_favorite(title)

@when(u'user adds {title} as favorite')
def when_add_favorite(context, title):
    #Make favorite
    context.catalog_page.make_favorite(title)

@then(u'{title} is favorite')
def then_is_favorite(context, title):
    #Verify that book is now favorite
    assert context.catalog_page.is_favorite(title)

@given(u'book has {state_of_book}')
def given_state_of_book(context, state_of_book):
    #Get first book in catalog
    book = context.catalog_page.get_books().first
    # get title and save to context
    context.title = context.catalog_page.get_title(book)
    #Handle cases where book starts as favorite
    if state_of_book == "favorite":
        #Make favorite and verify
        context.catalog_page.make_favorite(context.title)
        assert context.catalog_page.is_favorite(context.title)

@when (u'user clicks on heart button {times} times')
def when_many_clicks(context, times):
    #Convert example string to integer
    times = int(times)
    #Click on heart button as many times as example says
    for _ in range(times):
        context.catalog_page.click_heart_button(context.title)

@then(u'book should be {new_state}')
def then_new_state(context, new_state):
    #Verify each scenario
    if new_state == "favorite":
        assert context.catalog_page.is_favorite(context.title)
    else:
        assert not context.catalog_page.is_favorite(context.title)

@when(u'user marks the following books as favorites: {favorites}')
def when_favorites(context, favorites):
    if favorites == "<empty>":
        #Make an empty list of books
        books = []
    else:
        # Split list of favorites at the comma signs to make list of separate books,
        # then strip away spaces at beginning+end of each book in that list
        books = [book.strip() for book in favorites.split(",")]
    for book in books:
        #Make each book favorite
        context.catalog_page.make_favorite(book)
        # verify that each book is favorite
        assert context.catalog_page.is_favorite(book), f'Book "{book}" is not marked as favorite'

@when(u'navigates to "Mina böcker" page')
def when_go_to_my_books_page(context):
    #Go to "Mina böcker" page
    context.my_books_page.go_to_page()

@then(u'favorites list should have: {result}')
def then_display_favorites(context, result):
    # Handle special case (empty list)
    if result == "Empty list, info text":
        favorites_list = context.my_books_page.get_favorites_list_text()
        #List should be empty
        assert len(favorites_list) == 0
        # Verify that info text is displayed
        info_text = context.my_books_page.get_info_text()
        expect(info_text).to_be_visible()
    else:
        # Strip away spaces, split at comma and make list of separate books
        expected_books = [book.strip() for book in result.split(",")]
        # get actual list of books and strip
        displayed_books = context.my_books_page.get_favorites_list_text()
        assert displayed_books == expected_books

@given(u'{title} is favorite')
def given_is_favorite(context, title):
    #Make favorite
    context.catalog_page.make_favorite(title)
    #Verify that book is favorite
    assert context.catalog_page.is_favorite(title)

@when (u'user removes {title} from favorites')
def when_remove_favorite(context, title):
    #remove favorite
    context.catalog_page.remove_favorite(title)

@then(u'{title} is not favorite')
def then_is_not_favorite(context, title):
    #verify that book is no longer favorite
    assert not context.catalog_page.is_favorite(title)

@then(u'{title} does not exist in list of favorites on the "Mina böcker" page')
def then_book_is_not_in_list(context, title):
    #search for book in list of favorites
    favorite_item = context.my_books_page.get_specific_favorite(title)
    #Verify that book is not found
    assert favorite_item is None