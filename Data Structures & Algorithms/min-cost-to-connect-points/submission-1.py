class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0

        N = len(points)
        # i : list of [cost, node]
        adj = { i: [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm
        res = 0
        visited = set()
        minH = [[0, 0]] # [cost, point]

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            visited.add(i)
            res+=cost 

            for n_cost, neighbour in adj[i]:
                if neighbour not in visited:
                    heapq.heappush(minH, [n_cost, neighbour])
        return res
        