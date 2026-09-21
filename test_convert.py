import unittest

def convert(input):
    if input[0] == "C":
        return len(input) * 100
    if input[0] == "X":
        return len(input) * 10
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

    def test_c(self):
        self.assertEqual(convert("C"), 100)

    def test_cc(self):
        self.assertEqual(convert("CC"), 200)

    def test_ccc(self):
        self.assertEqual(convert("CCC"), 300)

if __name__ == "__main__":
    unittest.main()

