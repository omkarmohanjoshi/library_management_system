from logging_config import configure_logger
from typing import Tuple, Optional

# Set up logging
logger = configure_logger(__name__)

def get_choice() -> str:
    """Get the user's menu choice and validate it."""
    while True:
        try:
            print("\nLibrary Management System")
            # Menu options
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Search Book")
            print("5. List Books")
            print("6. Add User")
            print("7. Update User")
            print("8. Delete User")
            print("9. List Users")
            print("10. Search User")
            print("11. Checkout Book")
            print("12. Return Book")
            print("13. Exit")
            choice = input("Enter choice: ")
            if choice in [str(i) for i in range(1, 14)]:
                return choice
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            logger.error(f"Error getting choice: {e}")

def get_book_details() -> Tuple[str, str, str]:
    """Get book details from the user and validate them."""
    try:
        # Add input validation as needed
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        return title, author, isbn
    except Exception as e:
        logger.error(f"Error getting book details: {e}")

def get_user_details() -> Tuple[str, str]:
    """Get user details from the user and validate them."""
    try:
        # Add input validation as needed
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        return name, user_id
    except Exception as e:
        logger.error(f"Error getting user details: {e}")

def get_checkout_details(UserManager, BookManager) -> Tuple[Optional[str], Optional[str]]:
    """Get checkout details from the user and validate them."""
    try:
        # Add input validation as needed
        user_id = input("Enter user ID: ")
        user = UserManager.search_items(user_id=user_id)
        isbn = input("Enter ISBN of the book to checkout: ")
        book = BookManager.search_items(isbn=isbn)
        if user is None:
            print("User not found.")
        elif book is None:
            print("Book not found.")
        else:
            return user, book
        return None, None
    except Exception as e:
        logger.error(f"Error getting checkout details: {e}")


def return_details() -> Tuple[Optional[str], Optional[str]]:
    """Get return details from the user"""
    # Add input validation as needed
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to checkout: ")
    return user_id, isbn