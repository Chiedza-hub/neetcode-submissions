class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones, zeros = 0, 0
        diff_idx = {} # diff -> ones - zeros : index found
        res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            if n == 1:
                ones += 1
            # keep track of this suffix 
            if ones - zeros not in diff_idx:
                diff_idx[ones - zeros] = i

            if ones == zeros:
                res = max(res, ones + zeros)
            else:
                # get the prefix to remove (is zero is we just added diff)
                idx = diff_idx[ones - zeros]
                res = max(res, i - idx)
        return res 


        

