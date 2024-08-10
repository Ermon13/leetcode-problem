class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem_count ={}
        for num in nums:
            if num in elem_count:
                elem_count[num] +=1
            else:
                elem_count[num] = 1
        ans =[]
        for element,count in elem_count.items():
            if count > len(nums)//3:
                ans.append(element)
        return ans
            
        