import unittest

from run import get_ads


class TestScraperMethods(unittest.TestCase):

    def test_get_ads(self):
        ads = get_ads()
        self.assertIsInstance(ads, list)
        self.assertGreater(len(ads), 0)

if __name__ == '__main__':
    unittest.main()
