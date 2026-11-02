"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        

        res = []
        # put the first interval of each employee into a heap
        minHeap = [(emp[0].start, empId, 0) for empId, emp in enumerate(schedule)]
        heapq.heapify(minHeap)
        # find the earliest start time
        prevEnd = min(interval.start for emp in schedule for interval in emp)

        while minHeap:
            start, empId, jobIdx = heapq.heappop(minHeap)
            if prevEnd < start:
                res.append(Interval(prevEnd, start))
            # extend busy range 
            prevEnd = max(prevEnd, schedule[empId][jobIdx].end)
            # push the next interval from the same employee
            if jobIdx + 1 < len(schedule[empId]):
                heapq.heappush(minHeap, (schedule[empId][jobIdx + 1].start, empId, jobIdx + 1))

        return res