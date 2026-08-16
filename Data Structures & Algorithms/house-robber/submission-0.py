class Solution:
    def rob(self, nums: List[int]) -> int:
        amounts = [-1] * len(nums)
        def robrec(i):
            if i >= len(nums):
                return 0
            if amounts[i] != -1:
                return amounts[i]
            rob = nums[i] + robrec(i + 2)
            skip = robrec(i + 1)
            amounts[i] = max(rob, skip)
            return amounts[i]
        return robrec(0)