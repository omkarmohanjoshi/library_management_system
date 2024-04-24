import os
import json
from threading import Lock
from typing import Tuple, List, Dict
from logging_config import configure_logger
from book_management import book_manager_object, BookManager
from user_management import user_manager_object, UserManager
from checkout_management import checkout_manager_object, CheckoutManager

logger = configure_logger(__name__)

class DataStorage:
    DATA_FILE = 'library_data.json'
    data_lock = Lock()

    @staticmethod
    def load_data() -> Tuple[UserManager, BookManager, CheckoutManager]:
        with DataStorage.data_lock:
            try:
                if os.path.exists(DataStorage.DATA_FILE):
                    with open(DataStorage.DATA_FILE, 'r') as f:
                        data = json.load(f)
                        for user in data['users']:
                            user_manager_object.add_item(user['name'], user['user_id'])
                        for book in data['books']:
                            book_manager_object.add_item(book['title'], book['author'], book['isbn'])
                        for checkout in data['checkouts']:
                            user = user_manager_object.search_items(user_id=checkout['user_id'])
                            book = book_manager_object.search_items(isbn=checkout['isbn'])
                            if user and book:
                                checkout_manager_object.checkout_book(user, book)
                            else:
                                logger.error('Error loading checkout data: User or book not found')
                logger.info('Data loaded successfully from %s', DataStorage.DATA_FILE)
                return user_manager_object, book_manager_object, checkout_manager_object
            except (FileNotFoundError, json.JSONDecodeError) as e:
                logger.error('Error loading data from %s: %s', DataStorage.DATA_FILE, e)
                # return with empty data
                return user_manager_object, book_manager_object, checkout_manager_object

    @staticmethod
    def save_data(books: List[Dict[str, str]], users: List[Dict[str, str]], checkouts: List[Dict[str, str]]) -> None:
        with DataStorage.data_lock:
            try:
                with open(DataStorage.DATA_FILE, 'w') as f:
                    data = {
                        'books': books,
                        'users': users,
                        'checkouts': checkouts
                    }
                    json.dump(data, f)
                logger.info('Data saved successfully to %s', DataStorage.DATA_FILE)
            except Exception as e:
                logger.error('Error saving data to %s: %s', DataStorage.DATA_FILE, e)