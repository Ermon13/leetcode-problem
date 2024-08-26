class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        leng_word1 = len(word1)
        leng_word2 = len(word2)
        max_leng = max(leng_word1, leng_word2)
        for i in range(max_leng):
            if i < leng_word1:
                merged.append(word1[i])
            if i < leng_word2:
                merged.append(word2[i])
        merged = "".join(merged)
        return merged

