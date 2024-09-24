from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        i = 0
        result = [0] * len(s)

        while i < len(s):
            for d in dictionary:
                if d[0] == s[i]:
                    l = len(d)
                    if s[i : i + l] == d:
                        print(f"s[i:i+1] is {s[i:i+l]} and d is {d}")
                        for j in range(i, i + l):
                            result[j] = 1
            i += 1

        print(f"result is {result}")
        print(f"s[i] is {[s[i] for i in range(len(s)) if result[i] == 0]}")
        return len(s) - sum(result)


if __name__ == "__main__":
    s = Solution()
    print(s.minExtraChar("leetsccode", ["leet", "c"]))
    print(s.minExtraChar("sayhelloworld", ["hello", "world"]))
    print(
        s.minExtraChar(
            "kevlplxozaizdhxoimmraiakbak",
            [
                "yv",
                "bmab",
                "hv",
                "bnsll",
                "mra",
                "jjqf",
                "g",
                "aiyzi",
                "ip",
                "pfctr",
                "flr",
                "ybbcl",
                "biu",
                "ke",
                "lpl",
                "iak",
                "pirua",
                "ilhqd",
                "zdhx",
                "fux",
                "xaw",
                "pdfvt",
                "xf",
                "t",
                "wq",
                "r",
                "cgmud",
                "aokas",
                "xv",
                "jf",
                "cyys",
                "wcaz",
                "rvegf",
                "ysg",
                "xo",
                "uwb",
                "lw",
                "okgk",
                "vbmi",
                "v",
                "mvo",
                "fxyx",
                "ad",
                "e",
            ],
        )
    )
