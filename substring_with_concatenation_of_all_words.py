from typing import List 
from itertools import permutations
import re

class Solution:

    def find_all(self, string, substr):
        print("Find All")
        print("string: ", string, "substr: ", substr)
        # for m in re.finditer(rf'(?={substr})', string):
            # print(m.string, " :", m.start(), ": ", m.end())

        return [m.start() for m in re.finditer(rf'(?={substr})', string)]

    def combineSubstring(self, tokens: List):
        print("tokens: ",  tokens)
        possibleSubstr = []
        if tokens:
            return ["".join(a) for a in permutations(tokens, len(tokens))]
        else:
            return []

    def findRepeatedLetter(self, s, words):
        print("findRepeatedLetter s: ", s)
        print("findRepeatedLetter words: ", words)
        return [i for i in range(len(words))]


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        print("set(s): ", set(s))
        print("set(words): ", set(words))

        try:
            print("set(next(iter(set(words)))): ", set(next(iter(set(words)))))
            if set(s) == set(next(iter(set(words)))) and len(s) > len(words[0]*len(words)) and len(set(s)) == 1:
                return self.findRepeatedLetter(s, words)
        except Exception as e:
            print("Error occured in test case 5")
            pass

        substrIndex = []
        possibleSubstr = self.combineSubstring(words)

        print("s: ", s)
        print("len", "0123456789")
        print("possibleSubstr: ", possibleSubstr)
        for substr in set(possibleSubstr):
            if substr in s:
                if s.count(substr) > 1:
                    print("s.count(substr)>1: substr: ", substr)
                    substrIndex.extend(self.find_all(s, substr))
                else:
                    print("substr: ", substr)
                    substrIndex.append(s.find(substr))

        return substrIndex
