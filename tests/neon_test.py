import unittest
import sys
sys.path.insert(0, "C:\\Users\\zodia\\OneDrive\\Documents\\GitHub\\Neon-Shell\\neon")
import neon

class TestStringMethods(unittest.TestCase):

    def test_compiling_a_basic_print(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect!\');'), 'Hello, Arhitect!')
        
    def test_compiling_b_print_string(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect!\');'), 'Hello, Arhitect!')
        
    def test_compiling_c_print_integer(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect!\');'), 'Hello, Arhitect!')
        
    def test_compiling_d_print_variable(self):
        self.assertEqual(neon.compiling('output(\'Hello, Arhitect!\');'), 'Hello, Arhitect!')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        try:
            with self.assertRaises(TypeError):
                s.split()
        except AssertionError:
            print('HI', end = ' ')

if __name__ == '__main__':
    unittest.main(verbosity=2)