import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json

class TestBookInfo(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()

    def test_get_book_info(self):
        """Unit test to get details of a specific book"""

        expected = {
            'id': 1,
            'title': 'Book A',
            'genre': 'Genre A',
            'author': 'John Doe',
            'page_count': 100,
            'publisher': 'Publisher A',
            'value': 99.99,
            'pub_date': '2024-03-16'
        }
        actual = self.get_rest_call('http://localhost:5000/book/1') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_BOOK_INFO PASS")

    def test_get_nonexistent_book_info(self):
        """Unit test to get details of a book that does not exist"""
        expected = "Book not found"
        actual = self.get_rest_call('http://localhost:5000/book/999') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_NONEXISTENT_BOOK_INFO PASS")

    def get_rest_call(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text