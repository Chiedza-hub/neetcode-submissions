"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        N = len(intervals)
        s = 0
        e = 0
        count = 0
        max_count = 0

        while s < N:
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                # end is greater or equal so subtract 
                count -= 1
                e += 1
            max_count = max(max_count, count)

        return max_count


