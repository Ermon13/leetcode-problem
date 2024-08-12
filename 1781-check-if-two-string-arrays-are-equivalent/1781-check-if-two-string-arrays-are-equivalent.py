class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_1 = "".join(word1)
        word_2 = "".join(word2)
        if word_1 == word_2:
            return True
        else:
            return False