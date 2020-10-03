import unittest
from sample_modules import Adder

ADDER_NUM = 3
ADD_VAR = 2

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # do something for setup of test methods
        self.adder = Adder(ADDER_NUM)

    @unittest.skip('skip trial first')
    # test method name should start with 'test'
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_add_two(self):
        self.assertEqual(ADDER_NUM + ADD_VAR, self.adder.add_two(ADD_VAR))
        with self.assertRaises(TypeError):
            self.adder.add_two('aaa')
            # add_two(3)

if __name__ == "__main__":
    unittest.main()