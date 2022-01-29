import unittest

from serch import search_address


def serch(zipcode):
    address = search_address(zipcode)
    return (address)


class MyTestCase(unittest.TestCase):
    def test_SERCH(self):
        actual = search_address(zipcode="0287111")
        expected = "岩手県八幡平市大更"
        self.assertEqual(actual, expected)
        # add assertion here


if __name__ == '__main__':
    unittest.main()
