class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        for i in range(len(nums)):
            self.prefixSum.append(self.prefixSum[i] + nums[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]

