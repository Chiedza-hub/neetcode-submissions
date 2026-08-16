class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r :
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    # go right
                    l = m + 1
                else:
                    #go left
                    r = m -1
            # right sorted portion
            else: 
                if target < nums[m] or target > nums[r]: 
                    # go left
                    r = m - 1
                else:
                    # go right
                    l = m + 1

        return -1 # not found
        