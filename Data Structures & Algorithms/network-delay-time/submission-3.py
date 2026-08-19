
import heapq 
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        visited = set()
        min_t = 0
        min_heap = [(0, k)]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            min_t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
            
        return min_t if len(visited) == n else -1
        









        