from behave import given, when, then
from playwright.sync_api import expect

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

@given(u'{book} is not favorite')
def given_is_not_favorite(context, book):
    #Verify that book is NOT favorite
    assert not context.catalog_page.is_favorite(book)

@when(u'user adds {book} as favorite')
def when_add_favorite(context, book):
    #Make favorite
    context.catalog_page.make_favorite(book)

@then(u'{book} is favorite')
def then_is_favorite(context, book):
    #Verify that book is now favorite
    assert context.catalog_page.is_favorite(book)

@given(u'the following books are marked as favorites: {favorites}')
def given_favorites(context, favorites):
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

@when(u'user navigates to "Mina böcker" page')
def when_go_to_my_books_page(context):
    #Go to "Mina böcker" page
    context.my_books_page.go_to_page()

@then(u'favorites list should display: {result}')
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

@given(u'{book} is favorite')
def given_is_favorite(context, book):
    #Make favorite
    context.catalog_page.make_favorite(book)
    #Verify that book is favorite
    assert context.catalog_page.is_favorite(book)

@when (u'user removes {book} from favorites')
def when_remove_favorite(context, book):
    #remove favorite
    context.catalog_page.remove_favorite(book)

@then(u'{book} is not favorite')
def then_is_not_favorite(context, book):
    #verify that book is no longer favorite
    assert not context.catalog_page.is_favorite(book)

@then(u'{book} does not exist in list of favorites on the "Mina böcker" page')
def then_book_is_not_in_list(context, book):
    #search for book in list of favorites
    favorite_item = context.my_books_page.get_favorite(book)
    #Verify that book is not found
    assert favorite_item is None