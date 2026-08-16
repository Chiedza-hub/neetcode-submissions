class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}  # val : index

        for i in range(len(nums)):
            num = target - nums[i] 
            if num in mp:
                return [mp[num], i]
            mp[nums[i]] = i
        return
        

        