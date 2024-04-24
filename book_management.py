from logging_config import configure_logger
from typing import Optional, List, Dict
from models import BaseManager

logger = configure_logger(__name__)

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class BookManager(BaseManager):
    def add_item(self, title: str, author: str, isbn: str) -> None:
        try:
            self.items.append(Book(title, author, isbn))
            logger.info(f"Book added: {title}, {author}, {isbn}")
        except Exception as e:
            logger.error(f"Error adding book: {e}")

    def update_item(self, isbn: str, title: Optional[str] = None, author: Optional[str] = None) -> bool:
        try:
            for book in self.items:
                if book.isbn == isbn:
                    if title:
                        book.title = title
                    if author:
                        book.author = author
                    logger.info(f"Book updated: {isbn}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error updating book: {e}")
            return False

    def delete_item(self, isbn: str) -> bool:
        try:
            for book in self.items:
                if book.isbn == isbn:
                    self.items.remove(book)
                    logger.info(f"Book deleted: {isbn}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error deleting book: {e}")
            return False

    def list_items(self) -> List[Dict[str, str]]:
        try:
            return [book.__dict__ for book in self.items]
        except Exception as e:
            logger.error(f"Error listing books: {e}")
            return []

    def search_items(self, title: Optional[str] = None, author: Optional[str] = None, isbn: Optional[str] = None) -> Optional[Book]:
        try:
            for book in self.items:
                if ((title and book.title == title) or
                    (author and book.author == author) or
                    (isbn and book.isbn == isbn)):
                    return book
            return None
        except Exception as e:
            logger.error(f"Error searching books: {e}")
            return None
        
book_manager_object = BookManager()