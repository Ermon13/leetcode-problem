class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        count = 0
        for i in nums:
            count += i
            out.append(count)
        return out
        