import random
import unittest, main, lotto_page, Currency


class TestLogin(unittest.TestCase):

    def testPlayerId(self):
        testname = "Jared"
        testemail = "example@iwebtest.com"
        test_id = 77777777777777
        for i in range(len(testname)):
            self.assertEqual(13, (test_id), "If ID is not equal to the length 13")


    if __name__ == "__main__":
        unittest.main()



