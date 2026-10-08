import unittest


class Convert:
    def __init__(self):
        self.map = { "L": 50, "X": 10, "V": 5 }

    @classmethod
    def convert(cls, theRomanString):
        if len(theRomanString) > 1:
            #for (symbol, value) in cls.map:
            #  pass

            if theRomanString.find("L") == 1:
                return 50 - Convert.convert(theRomanString[:1])
            if theRomanString.find("L") == 0:
                return 50 + Convert.convert(theRomanString[1:])

            if theRomanString.find("X") == 1:
                return 10 - Convert.convert(theRomanString[:1])
            if theRomanString.find("X") == 0:
                return 10 + Convert.convert(theRomanString[1:])

            if theRomanString.find("V") == 0:
                return 5 + Convert.convert(theRomanString[1:])
            if theRomanString.find("V") == 1:
                return 5 - Convert.convert(theRomanString[:1])
        if theRomanString == "V":
            return 5
        if theRomanString == "X":
            return 10
        if theRomanString == "L":
            return 50
        return len(theRomanString)


class TestConvert(unittest.TestCase):
    def test_i(self):
        self.assertEqual(1, Convert.convert("I"))

    def test_iv(self):
        self.assertEqual(4, Convert.convert("IV"))

    def test_v(self):
        self.assertEqual(5, Convert.convert("V"))

    def test_vi(self):
        self.assertEqual(6, Convert.convert("VI"))

    def test_ii(self):
        self.assertEqual(2, Convert.convert("II"))

    def test_vii(self):
        self.assertEqual(7, Convert.convert("VII"))

    def test_viii(self):
        self.assertEqual(8, Convert.convert("VIII"))

    def test_X(self):
        self.assertEqual(10, Convert.convert("X"))

    def test_IX(self):
        self.assertEqual(9, Convert.convert("IX"))

    def test_XI(self):
        self.assertEqual(11, Convert.convert("XI"))

    def test_XIV(self):
        self.assertEqual(14, Convert.convert("XIV"))

    def test_XV(self):
        self.assertEqual(15, Convert.convert("XV"))

    def test_XVI(self):
        self.assertEqual(16, Convert.convert("XVI"))

    def test_XVIII(self):
        self.assertEqual(18, Convert.convert("XVIII"))

    def test_XIX(self):
        self.assertEqual(19, Convert.convert("XIX"))

    def test_XX(self):
        self.assertEqual(20, Convert.convert("XX"))

    def test_XXXIX(self):
        self.assertEqual(39, Convert.convert("XXXIX"))

    def test_L(self):
        self.assertEqual(50, Convert.convert("L"))

    def test_IL(self):
        self.assertEqual(49, Convert.convert("IL"))

    def test_LI(self):
        self.assertEqual(51, Convert.convert("LI"))


if __name__ == "__main__":
    unittest.main()

