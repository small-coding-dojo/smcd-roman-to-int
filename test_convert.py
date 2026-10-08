import unittest


class Convert:
    @classmethod
    def convert(cls, theRomanString):
        if len(theRomanString) > 1:
          if theRomanString.find("V") == 0:
                return 5 + Convert.convert(theRomanString[1:])
          if theRomanString.find("V") == 1:
                return 5 - Convert.convert(theRomanString[:1])
        if theRomanString == "V":
            return 5
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

if __name__ == "__main__":
    unittest.main()

