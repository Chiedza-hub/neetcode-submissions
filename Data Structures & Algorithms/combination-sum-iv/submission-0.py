class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = { 0 : 1}

        def dfs(total):
            if total in mem:
                return mem[total]

            res = 0
            for num in nums:
                if total - num >= 0:
                    res += dfs(total - num)

            mem[total] = res
            return res

        return dfs(target)
                    

        



