class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in Seen:
                return [Seen[diff], i]
            
            Seen[num] = i