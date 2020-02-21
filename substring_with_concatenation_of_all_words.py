from typing import List 
from itertools import permutations
import re 

class Solution:

    def find_all(self, string, substr):
        return [m.start() for m in re.finditer(rf'(?={substr})', string)]

    def combineSubstring(self):
        possibleSubstr = []
        if self.words:
            return ["".join(a) for a in permutations(self.words, len(self.words))]
        else:
            return []

    def findRepeatedLetter(self):
        return [i for i in range(len(self.words))]


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.s = s
        self.words = words
        try:
            if set(s) == set(next(iter(set(words)))) and len(s) > len(words[0]*len(words)) and len(set(s)) == 1 and len(set(s)) == len(set(words)):
            # if set("".join(i for i in set(words))) == set(s):
                return self.findRepeatedLetter()
        except Exception as e:
            pass


        substrIndex = []
        possibleSubstr = self.combineSubstring()

        for substr in set(possibleSubstr):
            if substr in s:
                if s.count(substr) > 1:
                    substrIndex.extend(self.find_all(s, substr))
                else:
                    # if possibleSubstr.count(substr) > 1:
                    substrIndex.extend(m.start() for m in re.finditer(rf'(?={substr})', s))
                    # else:
                        # substrIndex.append(s.find(substr))

        return substrIndex
