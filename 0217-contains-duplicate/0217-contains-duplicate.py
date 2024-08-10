class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = Counter(nums)
        for cnt in temp.values():
            if cnt > 1:
                return True
        return False

        