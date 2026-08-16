class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k 
        length = len(nums)
        res = [0] * (length - k + 1)
        
        while r <= length:
            if r == length:
                num = max(nums[l:])
            else:
                num = max(nums[l:r])
            res[l] = num
            l += 1
            r += 1
        
        return res