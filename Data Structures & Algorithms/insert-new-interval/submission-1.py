class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res =[]
        heapq.heapify(intervals)
        start, end = heapq.heappop(intervals)
        res.append([start, end])

        while intervals:  
            prev_start, prev_stop = res[-1]
            curr_start, curr_stop = heapq.heappop(intervals)
            # if overlap 
            if curr_start <= prev_stop:
                # merge and overwrite last element
                new_start = min(prev_start, curr_start)
                new_end = max(prev_stop, curr_stop)
                res.pop()
                res.append([new_start, new_end])
            else:
                res.append([curr_start, curr_stop])

        return res



        

        
                
                
        