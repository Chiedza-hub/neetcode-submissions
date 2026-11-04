from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqMap = defaultdict(list)

        for i, eq in enumerate(equations):
            neum, denom = eq
            eqMap[neum].append([denom, values[i]])
            eqMap[denom].append([neum, 1 / values[i]])

        def bfs(src, dest):
            if src not in eqMap or dest not in eqMap:
                return -1
            
            q = deque()
            visited = set()

            q.append([src, 1]) # node and curr_weight multiplied 
            visited.add(src)

            while q:
                a, w = q.popleft()
                if a == dest:
                    return w
                for b, weight in eqMap[a]:
                    if b not in visited:
                        q.append([b, w * weight])
                        visited.add(b)
            return -1
        
        return [bfs(src, dest) for src, dest in queries]

        



        