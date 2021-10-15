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

    def test_post_task(self):
        response = self.test_client.post('/task', json={"name": "買晚餐"}, follow_redirects=True)
        self.assertEqual(response.get_data(), b'{"result":{"id":1,"name":"\\u8cb7\\u665a\\u9910","status":false}}\n')
        self.assertEqual(response.status_code, 201)
