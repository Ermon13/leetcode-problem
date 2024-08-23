class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        word1 = []
        word2 = []
        for i in s:
            if i != '#':
                word1.append(i)
            elif word1:
                word1.pop()
        for j in t:
            if j != '#':
                word2.append(j)
            elif word2:
                word2.pop()
    # word1 = str(word1)
    # word2 = str(word2)
        return word1 == word2


                
        