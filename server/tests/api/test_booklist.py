import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json

class TestBooklist(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()

    def test_get_book(self):
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
        print("TEST_GET_BOOK PASS")

    def test_get_nonexistent_book(self):
        """Unit test to get details of a book that does not exist"""
        expected = "Book not found"
        actual = self.get_rest_call('http://localhost:5000/book/999') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_NONEXISTENT_BOOK PASS")

    def test_add_review(self):
        """Unit test to add a review for a book"""
        print("\nTEST_ADD_REVIEW")

        # prepare review content
        review_content = "This book is amazing!"

        # make request
        result = self.post_rest_call("http://localhost:5000/book/1/review", review_content)
        self.assertEqual(result, "Review added successfully")  
        print("TEST_ADD_REVIEW PASS")

    def test_add_to_reading_list(self):
        """Unit test to add a book to the reading list"""
        print("\nTEST_ADD_TO_READING_LIST")

        # prepare user id
        user_id = 1

        # make request
        result = self.post_rest_call("http://localhost:5000/book/1/add_to_reading_list", user_id)
        self.assertEqual(result, "Book added to reading list successfully")  
        print("TEST_ADD_TO_READING_LIST PASS")
    
    def get_rest_call(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def post_rest_call(self, url, data):
        response = requests.post(url, data=data)
        return response.text