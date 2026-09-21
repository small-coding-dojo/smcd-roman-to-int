import unittest

def convert(input):
    return len(input)

class TestConvert(unittest.TestCase):
    def test_i(self):
        self.assertEqual(convert("I"), 1)

    def test_ii(self):
        self.assertEqual(convert("II"), 2)

    def test_iii(self):
        self.assertEqual(convert("III"), 3)

if __name__ == "__main__":
    unittest.main()

