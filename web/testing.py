import unittest


from app import create_app


class OrmTestCase(unittest.TestCase):
    def setUp(self):
        self.app_instance = create_app(True)
        pass

    def tearDown(self):
        pass
