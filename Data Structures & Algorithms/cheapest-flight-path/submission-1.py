import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list)
        for s, d, c in flights:
            dic[s].append((d, c))
        heap = [[0, src, 0]] # [cost, airport, stops]
        
        visited = {}
        while heap:
            cost, airport, stops = heapq.heappop(heap)
            if stops > k + 1:
                continue
            if airport == dst:
                return cost
            if airport in visited and visited[airport] <= stops: 
                continue
            visited[airport] = stops
            for dest, price in dic[airport]:
                heapq.heappush(heap, [cost + price, dest, stops + 1])

        return -1