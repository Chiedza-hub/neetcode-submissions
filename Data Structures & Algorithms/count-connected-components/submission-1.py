from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in edgeMap[node]:
                if nei not in seen:
                    dfs(nei)

        count = 0
        for node in edgeMap:
            if node not in seen:
                count += 1
                dfs(node)

        if len(seen) < n:
            return count + (n - len(seen))

        return count 


