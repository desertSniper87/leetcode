from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in range( min(map(len, strs)) ):
            if len(set(list(map(lambda x: x[i], strs)))) == 1:
                result += strs[0][i]
            else:
                break

        return result
