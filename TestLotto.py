import unittest, lotto_page
import random


class TestLotto(unittest.TestCase):
        def testLotto(self):
            lotto = random.sample((1, 5), 3)
            self.assertEqual(5, (lotto), "Generate random numbers")


if __name__ == '__lotto_page__':
    unittest.main()
