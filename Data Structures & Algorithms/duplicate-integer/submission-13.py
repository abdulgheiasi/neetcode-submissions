class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = set(nums)
        return len(list) != len(nums)