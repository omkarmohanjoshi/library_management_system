import unittest
from user_management import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_add_item(self):
        self.user_manager.add_item('John', '1')
        self.assertEqual(len(self.user_manager.items), 1)
        self.assertEqual(self.user_manager.items[0].name, 'John')
        self.assertEqual(self.user_manager.items[0].user_id, '1')

    def test_update_item(self):
        self.user_manager.add_item('John', '1')
        self.user_manager.update_item('1', 'Jane')
        self.assertEqual(self.user_manager.items[0].name, 'Jane')

    def test_delete_item(self):
        self.user_manager.add_item('John', '1')
        self.user_manager.delete_item('1')
        self.assertEqual(len(self.user_manager.items), 0)

    def test_list_items(self):
        self.user_manager.add_item('John', '1')
        self.user_manager.add_item('Jane', '2')
        users = self.user_manager.list_items()
        self.assertEqual(len(users), 2)

    def test_search_items(self):
        self.user_manager.add_item('John', '1')
        self.user_manager.add_item('Jane', '2')
        user = self.user_manager.search_items('John')
        self.assertEqual(user.name, 'John')
        self.assertEqual(user.user_id, '1')

if __name__ == '__main__':
    unittest.main()