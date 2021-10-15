import os
import unittest

from app import create_app


class OrmTest(unittest.TestCase):
    def setUp(self):
        self.test_client = create_app(True).test_client()

    def tearDown(self):
        if os.path.exists("testing.db"):
            os.remove("testing.db")

    def test_index(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b"Hello, World!")
