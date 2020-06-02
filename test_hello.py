import unittest
from app import app

class TestHelloWord(unittest.TestCase):
    def test_hello_world_success(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        
        expected_output = "Hello World!"
        output = response.data.decode("utf-8")
        self.assertEqual(output, expected_output)

        response = app.test_client().get('/index')
        self.assertEqual(response.status_code, 200)

        output = response.data.decode("utf-8")
        self.assertEqual(output, expected_output)