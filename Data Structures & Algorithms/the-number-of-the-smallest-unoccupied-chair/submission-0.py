import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for idx, time in enumerate(times):
            time.append(idx)
        
        arrivals = sorted((time[0], time[2]) for time in times)
        departures = sorted((time[1], time[2]) for time in times)

        seating = {}
        # pointers to indexes
        arrive = 0
        leave = 0

        seat = 0

        heap = []
        while arrive < len(times):
            if arrivals[arrive][0] < departures[leave][0]:
                # seat the person 
                person = arrivals[arrive][1]
                if not heap:
                    seating[person] = seat
                    seat += 1
                else:
                    seating[person] = heapq.heappop(heap)
                arrive += 1

                if person == targetFriend:
                    return seating[person]
            else:
                # someone is leaving 
                person = departures[leave][1]
                heapq.heappush(heap, seating[person])
                leave += 1
                del seating[person]


            

