class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        result = []

        def combinations(i, arr, total):
            if total == target:
                result.append(arr)
                return 

            if i >= len(nums) or total > target:
                return
            
            # include 
            combinations(i + 1, arr + [nums[i]], total + nums[i])
            
            # exclude
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            combinations(i + 1, arr, total)
            
            
        combinations(0, [], 0)
        return result
