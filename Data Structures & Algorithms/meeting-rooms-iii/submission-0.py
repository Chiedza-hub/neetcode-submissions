class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # give first meeting to room 0
        available = [i for i in range(n)] 
        used = [] # end, room
        counts = [0 for i in range(n)]

        for start, end in sorted(meetings):
            # pop from used if meeting ended 
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            # if nothing is available
            if not available:
                last_end, room = heapq.heappop(used)
                end = last_end + (end - start)
                heapq.heappush(available, room)
            # assign a room
            next_room = heapq.heappop(available)
            heapq.heappush(used, (end, next_room))
            counts[next_room] += 1
        
        return counts.index(max(counts)) # get the index of the first occurance of the max


        


