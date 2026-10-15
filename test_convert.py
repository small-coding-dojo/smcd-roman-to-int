import unittest

map = {
    "L": "XXXXX",
    "X": "VV",
    "V": "IIIII"
}

def convert(input: str) -> int:
    def convert_reversed(roman: str, previous: int = 0) -> int:
        if not roman:
            return 0

        symbol = roman[0]
        value = convert(map[symbol]) if symbol in map else 1
        total = -value if value < previous else value

        return total + convert_reversed(roman[1:], max(value, previous))

    return convert_reversed(input[::-1])

class TestConvert(unittest.TestCase):
    def test_i(self):
        result = convert("I")
        self.assertEqual(result, 1)

    def test_ii(self):
        result = convert("II")
        self.assertEqual(result, 2)

    def test_iii(self):
        result = convert("III")
        self.assertEqual(result, 3)

    def test_v(self):
        result = convert("V")
        self.assertEqual(result, 5)

    def test_vi(self):
        result = convert("VI")
        self.assertEqual(result, 6)

    def test_vii(self):
        result = convert("VII")
        self.assertEqual(result, 7)

    def test_x(self):
        result = convert("X")
        self.assertEqual(result, 10)
    
    def test_xl(self):
        result = convert("XL")
        self.assertEqual(result, 40)

    def test_l(self):
        result = convert("L")
        self.assertEqual(result, 50)

    def test_iv(self):
        result = convert("IV")
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()

