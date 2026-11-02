import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        heap = intervals
        heapq.heapify(heap)
        result = []

        while heap:
            start, stop = heapq.heappop(heap)
            while heap and heap[0][0] <= stop:
                new_start, new_stop = heapq.heappop(heap)
                if new_stop > stop: 
                    stop = new_stop
            result.append([start, stop])

        return result


        