import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json

class TestBooklist(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()


    def test_get_nonexistent_book(self):
        """Unit test to get details of a book that does not exist"""
        expected = "Book not found"
        actual = self.get_rest_call('http://localhost:5000/book/999') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_NONEXISTENT_BOOK PASS")


    def get_rest_call(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def post_rest_call(self, url, data):
        response = requests.post(url, data=data)
        return response.text