import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0], x[1]))
        result = [intervals[0]]

        for start, stop in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], stop)
            else:
                result.append([start, stop])

        return result


        