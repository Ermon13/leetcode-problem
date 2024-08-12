class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev_string= []
        for i in range(len(s)-1, -1, -1):
            rev_string.append(s[i])
        # return rev_string
        s.clear()
        for i in rev_string:
            s.append(i)
        return s