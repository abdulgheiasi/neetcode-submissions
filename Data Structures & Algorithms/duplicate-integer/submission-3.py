class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)

        changedToSet = set(nums)
        setLength = len(changedToSet)

        if length > setLength:
            return True
        return False