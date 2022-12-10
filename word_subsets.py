from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def checkSubset2(mainWord: str, subsetWord: str):
            if len(subsetWord) == 1:
                return subsetWord in mainWord

            for w2 in subsetWord:
                if w2 not in mainWord:
                    return False

                if subsetWord.count(w2) > 1 and subsetWord.count(w2) > mainWord.count(w2):
                    return False


            return True

        #  def checkSubset(mainWord: str, subsetWord: str):
            #  if len(subsetWord) == 1:
                #  return subsetWord in mainWord

            #  sub_i = 0
            #  main_i = 0
            #  while sub_i < len(subsetWord) and main_i < len(mainWord):
                #  print('a', sub_i, main_i)
                #  if mainWord[main_i] == subsetWord[sub_i]:
                    #  sub_i += 1

                #  if sub_i == len(subsetWord):
                    #  print('b')
                    #  return True

                #  main_i += 1

            return False


        ws1 = set(words1)
        ws2 = set(words2)

        res = words1[:]



        for w2 in ws2:
            for w1 in ws1:
                if w1 not in res:
                    #  print('m', w1, w2)
                    continue
                if not checkSubset2(w1, w2):
                    #  print('x', w1, w2)
                    res.remove(w1)


        return res


if __name__ == "__main__":
    s = Solution()
    
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]

    print(s.wordSubsets(words1, words2))

    #  words1 = ["amazon","apple","facebook","google","leetcode"]
    #  words2 = ["lo","eo"]

    #  print(s.wordSubsets(words1, words2))

    words1 = ["facebok"]
    words2 = ["e","oo"]

    print(s.wordSubsets(words1, words2))

