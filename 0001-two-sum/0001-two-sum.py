class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}  # Initialize an empty dictionary

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[num] = index  # Store the index of each number

        # Since the problem guarantees exactly one solution, this return statement is redundant
        return []
