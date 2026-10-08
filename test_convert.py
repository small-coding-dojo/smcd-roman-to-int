import unittest


class Convert:
    @classmethod
    def convert(cls, theRomanString):
        return 1


class TestConvert(unittest.TestCase):
    def test_i(self):
        self.assertEqual(1, Convert.convert("I"))


if __name__ == "__main__":
    unittest.main()

