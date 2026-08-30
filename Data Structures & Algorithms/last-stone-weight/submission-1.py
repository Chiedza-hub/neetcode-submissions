import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make a max heap
        nums = [-num for num in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            x = -heapq.heappop(nums)
            y = -heapq.heappop(nums)
            z = abs(x - y)
            
            if y != x: 
                heapq.heappush(nums, -(x - y))
        
        return -nums[0] if nums else 0