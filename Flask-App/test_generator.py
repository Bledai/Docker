import sys
import unittest

import generator

class TestFlaskApp(unittest.TestCase):
    """Test class for unittest"""
    def test_sample_single_word(self):
        l = ('foo', 'bar', 'foobar')
        words = generator.sample(l, 2)
        # test 1 word
        self.assertIn(generator.sample(l), l)
        # test multiple words
        self.assertEqual(len(words), 2)
        self.assertIn(words[0], l)
        self.assertIn(words[1], l)
        self.assertIsNot(words[0], words[1])

    def test_generate_buzz(self):
        self.assertGreaterEqual(len(generator.generate_buzz()), 5)


if __name__ == '__main__':
    unittest.main()
