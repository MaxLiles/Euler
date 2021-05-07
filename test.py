import unittest
from helper import *

class EulerTest(unittest.TestCase ):
    def testPalindrome(self):
        expected = isPalindrome(99)
        self.assertEqual( expected, True)
    def testNotPalindrome(self):
        expected = isPalindrome(98)
        self.assertEqual( expected, False)


if __name__ == '__main__':
    unittest.main()
