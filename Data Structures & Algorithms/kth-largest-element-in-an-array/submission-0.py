import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        heap = [-num for num in nums]
        heapq.heapify(heap)
        val = heapq.heappop(heap)
        n = 1
        while n < k and heap:
            val = heapq.heappop(heap)
            n += 1
        return -val 


        