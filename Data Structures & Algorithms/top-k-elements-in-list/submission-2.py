from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        # make frequency map 
        freqs = Counter(nums)
        # turn it into a maxheap 
        heap = [[-1 * freq, num] for num, freq in freqs.items()]
        heapq.heapify(heap)

        result = []
        while k > 0 and heap:
            neg_freq, num = heapq.heappop(heap)
            result.append(num)
            k -= 1
        
        return result 

        