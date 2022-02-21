import unittest
import sys
sys.path.insert(0, "C:\\Users\\Professional\\Documents\\GitHub\\Neon-Shell\\neon")
import neon

class TestStringMethods(unittest.TestCase):

    def test_compiling_a_basic_print(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect\' + \'!\');'), 'Hello, Arhitect!')

    def test_compiling_b_print_string(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect!\');'), 'Hello, Arhitect!')

    def test_compiling_c_print_integer(self):
        self.assertEqual(neon.compiling('output(0);'), '0')

if __name__ == '__main__':
    unittest.main(verbosity=2)
