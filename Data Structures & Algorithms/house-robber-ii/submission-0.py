class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]


        def rob_rec(arr):
            mem = [-1] * len(arr) 

            def helper(i):
                if i >= len(arr): 
                    return 0

                if mem[i] != -1:
                    return mem[i]

                robbed = arr[i] + helper(i + 2)
                skip = helper(i + 1)
                mem[i] = max(robbed, skip)
                return mem[i]
            return helper(0)
        
        first = rob_rec(nums[1:])
        sec = rob_rec(nums[:-1])

        return max(first, sec)