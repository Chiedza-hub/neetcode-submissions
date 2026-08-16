class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        my_nums = set()
        for num in sorted(nums):
            if num in my_nums:
                continue
            if num - 1 not in my_nums:
                count = 0
            my_nums.add(num)
            count += 1
            max_count = max(count, max_count)
        return max_count 



