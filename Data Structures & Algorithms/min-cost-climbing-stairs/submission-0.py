class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def costrec(n):
            if n >= len(cost):
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = cost[n] + min(costrec(n + 1), costrec(n + 2))
            return memo[n]
            
        return min(costrec(0), costrec(1))