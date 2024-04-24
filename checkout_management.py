import json
from logging_config import configure_logger
from typing import List, Dict, Optional, Any
from user_management import User
from book_management import Book
from models import BaseManager

# Set up logging
logger = configure_logger(__name__)

class Checkout:
    def __init__(self, user: User, book: Book):
        self.user = user
        self.book = book

    def __str__(self) -> str:
        return f"User id: {self.user.user_id}, Isbn: {self.book.isbn}"

class CheckoutManager(BaseManager):
    def checkout_book(self, user: User, book: Book) -> None:
        try:
            if book.available:
                self.items.append(Checkout(user, book))
                book.available = False
                logger.info(f"Book checked out: User id: {user.user_id}, Isbn: {book.isbn}")
            else:
                logger.error(f"Book is not available: Isbn: {book.isbn}")
        except Exception as e:
            logger.error(f"Error checking out book: {e}")

    def list_items(self) -> List[Dict[str, str]]:
        try:
            return [{ "user_id" : checkout.user.user_id, "isbn": checkout.book.isbn } for checkout in self.items]
        except Exception as e:
            logger.error(f"Error listing checkouts: {e}")
            return []

    def return_book(self, user_id: str, isbn: str) -> bool:
        try:
            for checkout in self.items:
                if checkout.user.user_id == user_id and checkout.book.isbn == isbn:
                    self.items.remove(checkout)
                    checkout.book.available = True
                    logger.info(f"Book returned: User id: {user_id}, Isbn: {isbn}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error returning book: {e}")
            return False

    def search_items(self, user_id: Optional[str] = None, isbn: Optional[str] = None) -> Optional[Checkout]:
        try:
            for checkout in self.items:
                if ((user_id and checkout.user.user_id == user_id) or
                    (isbn and checkout.book.isbn == isbn)):
                    return checkout
            return None
        except Exception as e:
            logger.error(f"Error searching checkouts: {e}")
            return None

    # Need to implement these methods from BaseManager to avoid TypeError        
    def add_item(self, item: Any) -> None:
        raise NotImplementedError("This method is not implemented.")

    def delete_item(self, item_id: Any) -> None:
        raise NotImplementedError("This method is not implemented.")

    def update_item(self, item_id: Any, **kwargs: Any) -> None:
        raise NotImplementedError("This method is not implemented.")
    

checkout_manager_object = CheckoutManager()