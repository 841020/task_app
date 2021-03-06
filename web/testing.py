import os
import unittest
import json

from app import create_app
from orm_controller import create_row, read_rows_list, read_row, update_row, delete_row
from models import Tasks


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        # Create an app instance that uses the test database
        self.test_client = create_app(True).test_client()

    def tearDown(self):
        if os.path.exists("testing.db"):
            os.remove("testing.db")

    def test_index(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data().decode(), "Hello, World!")

    def test_post_task(self):
        response = self.test_client.post('/task', json={"name": "買晚餐"}, follow_redirects=True)
        self.assertEqual(json.loads(response.get_data().decode()), {"result": {"id": 1, "name": "買晚餐", "status": False}})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        # Empty table
        response = self.test_client.get('/tasks')
        self.assertEqual(json.loads(response.get_data().decode()), {"result": []})
        self.assertEqual(response.status_code, 200)

        # add one row into db
        self.test_client.post('/task', json={"name": "買晚餐"}, follow_redirects=True)
        response = self.test_client.get('/tasks')
        self.assertEqual(json.loads(response.get_data().decode()), {"result": [{"id": 1, "name": "買晚餐", "status": False}]})
        self.assertEqual(response.status_code, 200)

    def test_put_task(self):
        # add one row into db
        self.test_client.post('/task', json={"name": "買晚餐"}, follow_redirects=True)
        response = self.test_client.put("/task/1", json={"name": "買早餐", "status": 1, "id": 1})
        self.assertEqual(json.loads(response.get_data().decode()), {"result": {"id": 1, "name": "買早餐", "status": True}})
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        # add one row into db
        self.test_client.post('/task', json={"name": "買晚餐"}, follow_redirects=True)
        response = self.test_client.delete('/task/1')
        self.assertEqual(response.status_code, 200)


class OrmTestCase(unittest.TestCase):
    '''This test case only focuses on the areas that the ApiTestCase does not cover in the unit test'''

    def setUp(self):
        # Create an app instance that uses the test database
        self.test_client = create_app(True).test_client()

    def tearDown(self):
        if os.path.exists("testing.db"):
            os.remove("testing.db")

    def test_create_row(self):
        exc_type, exc_obj, exc_tb = create_row(Tasks, {"status": 123})
        # testing column type error
        self.assertEqual(str(exc_type), "<class 'sqlalchemy.exc.StatementError'>")
        self.assertEqual(str(exc_obj), "(builtins.ValueError) Value 123 is not None, True, or False\n[SQL: INSERT INTO tasks (name, status) VALUES (?, ?)]\n[parameters: [{'status': 123, 'name': None}]]")

    def test_read_rows_list(self):
        exc_type, exc_obj, exc_tb = read_rows_list('123')
        # table not exist
        self.assertEqual(str(exc_type), "<class 'sqlalchemy.exc.ArgumentError'>")
        self.assertEqual(str(exc_obj), "Textual column expression '123' should be explicitly declared with text('123'), or use column('123') for more specificity")

    def test_read_row(self):
        # index id not exist
        exc_type, exc_obj, exc_tb = read_row(Tasks, 0)
        self.assertEqual(str(exc_type), "<class 'AttributeError'>")
        self.assertEqual(str(exc_obj), "'NoneType' object has no attribute '__dict__'")

    def test_update_row(self):
        exc_type, exc_obj, exc_tb = update_row(123, 0, {'status': True})
        self.assertEqual(str(exc_type), "<class 'sqlalchemy.exc.InvalidRequestError'>")
        self.assertEqual(str(exc_obj), 'Entity namespace for "123" has no property "id"')

    def test_delete_row(self):
        exc_type, exc_obj, exc_tb = delete_row(123, 0)
        self.assertEqual(str(exc_type), "<class 'sqlalchemy.exc.InvalidRequestError'>")
        self.assertEqual(str(exc_obj), 'Entity namespace for "123" has no property "id"')
