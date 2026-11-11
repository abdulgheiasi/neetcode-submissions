class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = []

        for i in range(len(nums)):
            if nums[i] in s:
                return True
            
            s.append(nums[i])
        return False