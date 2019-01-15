import app
import unittest

class UnitTests(unittest.TestCase):
    
    def test_a_test(self):
        self.assertEqual(app.test_func(),2)