class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                n += i
        return n == n[::-1]
            
        