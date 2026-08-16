class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        prefix = [1] * n 
        suffix = [1] * n
        # prefix
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]
        # suffix
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix[j] = 1
            else:
                suffix[j] = nums[j + 1] * suffix[j + 1]
        # join prefix and suffix 
        for k in range(len(nums)):
            res[k] = prefix[k] * suffix[k]
        
        return res