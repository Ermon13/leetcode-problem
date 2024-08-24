class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = {}
        majority_count = len(nums) // 2
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] > majority_count:
                return num
        return -1 