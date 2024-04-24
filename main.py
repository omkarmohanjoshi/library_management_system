import json
from logging_config import configure_logger
from cli_utils import get_choice, get_book_details, get_user_details, get_checkout_details
from storage import DataStorage

logger = configure_logger(__name__)

# Load data from storage
UserManager, BookManager, CheckoutManager = DataStorage.load_data()


# Save objects to json file
def save_data() -> None:
    """Save the current state of the system to the data file."""
    try:
        books = BookManager.list_items()
        users = UserManager.list_items()
        checkouts = CheckoutManager.list_items()
        DataStorage.save_data(books, users, checkouts)
        logger.info("Data saved successfully.")
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def main() -> None:
    while True:
        try:
            choice = get_choice()
            if choice == '1':
                # Add book
                title, author, isbn = get_book_details()
                BookManager.add_item(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                # Update book
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                if BookManager.update_item(isbn, title, author):
                    print("Book updated.")
                else:
                    print("Book not found.")
            elif choice == '3':
                # Delete book
                isbn = input("Enter ISBN of the book to delete: ")
                if BookManager.delete_item(isbn):
                    print("Book deleted.")
                else:
                    print("Book not found.")
            elif choice == '4':
                # Search book
                isbn = input("Enter ISBN of the book to search: ")
                book = BookManager.search_items(isbn=isbn)
                if book:
                    print(f"Book found: {book}")
                else:
                    print("Book not found.")
            elif choice == '5':
                # List books
                print("Books in the library:")
                print(json.dumps(BookManager.list_items(), indent=4))
            elif choice == '6':
                # Add user
                name, user_id = get_user_details()
                UserManager.add_item(name, user_id)
                print("User added.")
            elif choice == '7':
                # Update user
                user_id = input("Enter User ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                if UserManager.update_item(user_id, name):
                    print("User updated.")
                else:
                    print("User not found.")
            elif choice == '8':
                # Delete user
                user_id = input("Enter User ID to delete: ")
                if UserManager.delete_item(user_id):
                    print("User deleted.")
                else:
                    print("User not found.")
            elif choice == '9':
                # List users
                print("Users in the system:")
                print(json.dumps(UserManager.list_items(), indent=4))
            elif choice == '10':
                # Search users
                name = input("Enter name of the user to search (leave blank to skip): ")
                user_id = input("Enter User ID to search (leave blank to skip): ")
                user = UserManager.search_items(name=name if name else None, user_id=user_id if user_id else None)
                if user:
                    print(f"User found: {user}")
                else:
                    print("User not found.")
            elif choice == '11':
                # Checkout book
                user, book = get_checkout_details(UserManager, BookManager)
                if user is None or book is None:
                    print("Checkout failed.")
                else:
                    CheckoutManager.checkout_book(user, book)
                    print("Checkout successful.")
            elif choice == '12':
                # Return book
                user_id, isbn = get_checkout_details(UserManager, BookManager)
                CheckoutManager.return_book(user.user_id, book.isbn)
                print("Book returned successfully.")
            elif choice == '13':
                # Save data and exit
                save_data()
                print("Exiting.")
                break
        except Exception as e:
            logger.error(f"Error in main loop: {e}")

if __name__ == "__main__":
    main()