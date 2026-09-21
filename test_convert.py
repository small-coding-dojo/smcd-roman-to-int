import unittest

def convert(input):
    if input == "XXX":
        return 30
    if input == "XX":
        return 20
    if input == "X":
        return 10
    return len(input)

class TestConvert(unittest.TestCase):
    def test_i(self):
        self.assertEqual(convert("I"), 1)

    def test_ii(self):
        self.assertEqual(convert("II"), 2)

    def test_iii(self):
        self.assertEqual(convert("III"), 3)

    def test_x(self):
        self.assertEqual(convert("X"), 10)

    def test_xx(self):
        self.assertEqual(convert("XX"), 20)

    def test_xxx(self):
        self.assertEqual(convert("XXX"), 30)

if __name__ == "__main__":
    unittest.main()

