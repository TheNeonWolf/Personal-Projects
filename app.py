from utils import database

USER_CHOICE = """
ENTER:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your Choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_all_books()
        elif user_input == 'r':
            prompt_mark_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid Command. Please try again.")
        user_input = input(USER_CHOICE)

def prompt_add_book():
    book_name = input('Enter book name: ')
    book_author = input('Enter book author: ')

    database.add_book(book_name, book_author)

def prompt_list_all_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} , read: {read}")

def prompt_mark_as_read():
    name = input('Enter book name: ')
    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input('Enter book name: ')
    database.delete_book(name)

menu()