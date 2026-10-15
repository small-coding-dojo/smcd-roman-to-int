import unittest

map = {
    "L": "XXXXX",
    "X": "VV",
    "V": "IIIII"
}

def convert(input : string) -> int:
    if len(input) > 1:
        return convert(input[0]) + convert(input[1:])
    
    if input[0] != "I":
        return convert(map[input[0]])

    return len(input)

class TestConvert(unittest.TestCase):
    def test_i(self):
        result = convert("I")
        self.assertEqual(result, 1)

    def test_ii(self):
        result = convert("II")
        self.assertEqual(result, 2)

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

    def test_l(self):
        result = convert("L")
        self.assertEqual(result, 50)

if __name__ == "__main__":
    unittest.main()

