import unittest

roman_value = {
    "C": 100,
    "X": 10,
    "V": 5,
    "I": 1
}

def convert(input):
    reversed = input[::-1]
    
    result = 0
    previous = 1

    for symbol in reversed:
        current = roman_value[symbol]

        if current < previous:
            result -= current
        else:
            result += current
        
        previous = roman_value[symbol]

    return result

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

    def test_xi(self):
        self.assertEqual(convert("XI"), 11)

    def test_cx(self):
        self.assertEqual(convert("CX"), 110)

    def test_ci(self):
        self.assertEqual(convert("CI"), 101)

    def test_v(self):
        self.assertEqual(convert("V"), 5)

    def test_iv(self):
        self.assertEqual(convert("IV"), 4)

    def test_ix(self):
        self.assertEqual(convert("IX"), 9)

    def test_xc(self):
        self.assertEqual(convert("XC"), 90)

if __name__ == "__main__":
    unittest.main()

