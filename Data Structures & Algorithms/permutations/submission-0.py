class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        used = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue 
                
                used[i] = True
                permutation.append(nums[i])

                backtrack()

                permutation.pop()
                used[i] = False
        
        backtrack()
        return result
        