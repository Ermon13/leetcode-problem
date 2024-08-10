class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = {}
        majority_count = len(nums) // 2
        
        # Count the occurrences of each element
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            
            # Check if the current element is the majority element
            if count_dict[num] > majority_count:
                return num
        
        # Since the majority element always exists, we will never reach this line
        return -1 