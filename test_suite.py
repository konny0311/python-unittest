import unittest
from sample_test import TestStringMethods

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_add_two'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())