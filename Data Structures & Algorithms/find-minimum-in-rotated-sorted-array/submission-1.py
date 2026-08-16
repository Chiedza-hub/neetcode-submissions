class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            print(m)
            if nums[m] < nums[r]:
                r = m # search left
            else:
                l = m + 1 # search right
        print(l)
        return nums[l]