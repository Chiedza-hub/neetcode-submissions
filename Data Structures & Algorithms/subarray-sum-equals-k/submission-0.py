class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total = 0
        curr_sum = 0
        prefixes = { 0 : 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            # is there a prefix we have that can make this equal k?
            total += prefixes.get(diff, 0)
            # add this one as a prefix
            prefixes[curr_sum] = 1 + prefixes.get(curr_sum, 0)
        return total
        