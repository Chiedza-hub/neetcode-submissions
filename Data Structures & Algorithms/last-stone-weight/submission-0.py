import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make a max heap
        nums = [-1 * num for num in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = abs(x - y)
            
            if z == 0: 
                continue
            else:
                heapq.heappush(nums, -1 * z) 
        
        return -1 * nums[0] if len(nums) else 0