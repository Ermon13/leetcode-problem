class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n <= 1:
            return n
        else:
            for i in range(2,n+1):
                temp = a
                a = b
                b = b + temp
        return b
