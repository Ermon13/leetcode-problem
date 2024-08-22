class Solution:
    def isValid(self, s: str) -> bool:
        main_list = {'{':'}', '[':']','(':')'}
        stack = []
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif main_list[stack[-1]] != i:
                    return False
                stack.pop()
        return len(stack) == 0