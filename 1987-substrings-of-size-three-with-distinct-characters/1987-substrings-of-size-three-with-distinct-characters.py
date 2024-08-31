class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        k = 3
        good = []
        for i in range(n-2):
            sub = s[i:i+3]
            if len(set(sub)) == 3:
                good.append(sub)
        return len(good)

        