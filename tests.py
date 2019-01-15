import unittest
import run

class UnitTests(unittest.TestCase):

    def test_a_test(self):
        self.assertEqual(run.test_func(),2)