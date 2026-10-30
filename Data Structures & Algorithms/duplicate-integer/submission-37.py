class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
"""
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        
      """