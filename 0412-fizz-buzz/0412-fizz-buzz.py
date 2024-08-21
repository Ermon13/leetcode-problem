class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                num.append("FizzBuzz")
            elif i % 3 == 0:
                num.append("Fizz")
            elif i % 5 == 0:
                num.append("Buzz")
            else:
                i = str(i)
                num.append(i)
        return num