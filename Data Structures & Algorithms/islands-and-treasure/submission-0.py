from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
    
        dist = 0
        while queue:
            # process this level
            for p in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist
            
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and grid[ni][nj] != -1:
                        visited.add((ni, nj))
                        queue.append((ni, nj)) 

            dist += 1

    