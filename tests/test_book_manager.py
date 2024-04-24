import unittest
from book_management import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_item(self):
        self.book_manager.add_item('Book1', 'Author1', 'ISBN1')
        self.assertEqual(len(self.book_manager.items), 1)
        self.assertEqual(self.book_manager.items[0].title, 'Book1')
        self.assertEqual(self.book_manager.items[0].author, 'Author1')
        self.assertEqual(self.book_manager.items[0].isbn, 'ISBN1')

    def test_update_item(self):
        self.book_manager.add_item('Book1', 'Author1', 'ISBN1')
        self.book_manager.update_item('ISBN1', 'Book2', 'Author2')
        self.assertEqual(self.book_manager.items[0].title, 'Book2')
        self.assertEqual(self.book_manager.items[0].author, 'Author2')

    def test_delete_item(self):
        self.book_manager.add_item('Book1', 'Author1', 'ISBN1')
        self.book_manager.delete_item('ISBN1')
        self.assertEqual(len(self.book_manager.items), 0)

    def test_list_items(self):
        self.book_manager.add_item('Book1', 'Author1', 'ISBN1')
        self.book_manager.add_item('Book2', 'Author2', 'ISBN2')
        books = self.book_manager.list_items()
        self.assertEqual(len(books), 2)

    def test_search_items(self):
        self.book_manager.add_item('Book1', 'Author1', 'ISBN1')
        self.book_manager.add_item('Book2', 'Author2', 'ISBN2')
        book = self.book_manager.search_items('Book1', 'Author1', 'ISBN1')
        self.assertEqual(book.title, 'Book1')
        self.assertEqual(book.author, 'Author1')
        self.assertEqual(book.isbn, 'ISBN1')

if __name__ == '__main__':
    unittest.main()