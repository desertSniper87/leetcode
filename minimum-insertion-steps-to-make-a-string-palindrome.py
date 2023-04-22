def lcs(s1: str, s2: str) -> int:
    s1_l = len(s1)
    s2_l = len(s2)

    L = [[0 for _ in range(s2_l+1)] for _ in range(s1_l+1)]

    for s1_idx in range(s1_l+1):
        for s2_idx in range(s2_l+1):
            if s1_idx == 0 or s2_idx == 0:
                L[s1_idx][s2_idx] = 0

            elif s1[s1_idx - 1] == s2[s2_idx - 1]:
                L[s1_idx][s2_idx] = L[s1_idx - 1][s2_idx - 1] + 1

            else: 
                L[s1_idx][s2_idx] = max(L[s1_idx-1][s2_idx], L[s1_idx][s2_idx-1])

    return L[s1_l][s2_l]

class Solution:
    def minInsertions(self, s: str) -> int:
        lcs_ = lcs(s, s[::-1])
        return len(s) - len(lcs_)
