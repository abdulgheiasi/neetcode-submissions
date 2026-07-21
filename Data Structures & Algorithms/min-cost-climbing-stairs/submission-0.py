class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0

        for i in range(len(cost) - 1, -1, -1):
            current = cost[i] + min(one, two)
            two = one
            one = current
        
        return min(one, two)