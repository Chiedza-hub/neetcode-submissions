from collections import deque
import heapq

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        edgeMap = defaultdict(list)
        # get the map
        for node1, node2 in edges:
            edgeMap[node1].append(node2)
            edgeMap[node2].append(node1)
        # get the height given a root
        def get_height_bfs(root):
            visited = set()
            queue = deque()
            queue.append(root)
            height = 0

            while queue:
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    visited.add(node)
                    for neigh in edgeMap[node]:
                        if neigh not in visited:
                            queue.append(neigh)
                height += 1
            return height
        
        # try every possible root
        min_height = n
        result = []
        for node in edgeMap:
            height = get_height_bfs(node)
            if height == min_height:
                result.append(node)
            elif height < min_height:
                result = [node]
                min_height = height

        return result


        

