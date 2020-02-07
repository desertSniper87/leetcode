import unittest
from substring_with_concatenation_of_all_words import *


class StringTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_string_1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]

        self.assertCountEqual(self.solution.findSubstring(s, words), [0, 9] )
    def test_string_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]

        self.assertCountEqual(self.solution.findSubstring(s, words), [] )
    def test_string_3(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]

        self.assertCountEqual(self.solution.findSubstring(s, words), [8])

    def test_string_4(self):
       s = "foobarfoobar"
       words = ["foo","bar"] 

       self.assertCountEqual(self.solution.findSubstring(s, words), [0, 3, 6])


    def test_string_5(self):
        s = ""
        words = []

        self.assertEqual(self.solution.findSubstring(s, words), [])

    def test_string_6(self):
        s = "a"
        words = []

        self.assertEqual(self.solution.findSubstring(s, words), [])
    def test_string_6(self):
        s = "aaa"
        words = ["a","a"]

        self.assertEqual(self.solution.findSubstring(s, words), [0, 1])

    def test_string_7(self):
        s = "aaaaaaaa"
        words = ["aa","aa","aa"]

        self.assertEqual(self.solution.findSubstring(s, words), [0, 1, 2])
    def test_string_7(self):
        s = "aaa"
        words = ["aa","aa"]

        self.assertEqual(self.solution.findSubstring(s, words), [])

    def test_string_8(self):
        s = "aaa"
        words = ["a","b"]

        self.assertEqual(self.solution.findSubstring(s, words), [])
    def test_string_8(self):
        s = "ababaab"
        words = ["ab","ba","ba"]

        self.assertEqual(self.solution.findSubstring(s, words), [1])
    def test_string_9(self):
        s = "abababab"
        words = ["a","b","a"]

        self.assertEqual(self.solution.findSubstring(s, words), [0, 2, 4])
    def test_string_10(self):
        s = "abababab"
        words = ["ab","ab","ab"]

        self.assertEqual(self.solution.findSubstring(s, words), [0, 2, 4])
def main():
    unittest.main()


if __name__ == '__main__':
    main()

