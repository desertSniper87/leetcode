from typing import Dict, List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def get_dictionary_of_char_occuring(word: str):
            ret = {}
            for w in word:
                ret[w] = word.count(w)

            return ret

        def isASubString(word: str, dictionary: Dict):
            for d in dictionary:
                if word.count(d) < dictionary[d]:
                    return False

            return True




        count_of_str = {}

        for w in set(words2):
            dictionary = get_dictionary_of_char_occuring(w)
            for k in dictionary:
                count_of_str[k] = max(count_of_str[k], dictionary[k]) if count_of_str.get(k) else dictionary[k]

        #  for w in words1:
            #  if 



        return list(filter(lambda x: isASubString(x, count_of_str), words1))


if __name__ == "__main__":
    s = Solution()

    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]

    print(s.wordSubsets(words1, words2))

    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["lo", "eo"]

    print(s.wordSubsets(words1, words2))

    words1 = ["facebok"]
    words2 = ["e", "oo"]

    print(s.wordSubsets(words1, words2))

    words1 = ["amazon","apple","facebook","google","leetcode"]
    #  words2 = ["ec", "oc", "ceo"]
    words2 = ["ee", "oo", "ceo"]

    print(s.wordSubsets(words1, words2))
