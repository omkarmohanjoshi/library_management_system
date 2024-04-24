import unittest
from checkout_management import CheckoutManager
from user_management import User
from book_management import Book

class TestCheckoutManager(unittest.TestCase):
    def setUp(self):
        self.checkout_manager = CheckoutManager()
        self.user = User('John', '1')
        self.book = Book('Book1', 'Author1', 'ISBN1')

    def test_checkout_book(self):
        self.checkout_manager.checkout_book(self.user, self.book)
        self.assertEqual(len(self.checkout_manager.items), 1)
        self.assertEqual(self.checkout_manager.items[0].user.user_id, '1')
        self.assertEqual(self.checkout_manager.items[0].book.isbn, 'ISBN1')

    def test_list_items(self):
        self.checkout_manager.checkout_book(self.user, self.book)
        items = self.checkout_manager.list_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['user_id'], '1')
        self.assertEqual(items[0]['isbn'], 'ISBN1')

    def test_return_book(self):
        self.checkout_manager.checkout_book(self.user, self.book)
        result = self.checkout_manager.return_book('1', 'ISBN1')
        self.assertTrue(result)
        self.assertEqual(len(self.checkout_manager.items), 0)

    def test_search_items(self):
        self.checkout_manager.checkout_book(self.user, self.book)
        checkout = self.checkout_manager.search_items('1', 'ISBN1')
        self.assertEqual(checkout.user.user_id, '1')
        self.assertEqual(checkout.book.isbn, 'ISBN1')

if __name__ == '__main__':
    unittest.main()