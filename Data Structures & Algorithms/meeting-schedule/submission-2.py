"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        times = sorted(intervals,  key=lambda x: x.end)
        first_start, first_end = times[0].start, times[0].end
        for time in times[1:]:
            start, end = time.start, time.end
            if start < first_end:
                return False
            first_end = end
            first_start = start
        return True

