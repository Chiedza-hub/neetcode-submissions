from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        rows, cols = len(grid), len(grid[0])

        def find_island(i, j):
             queue = deque([(i, j)])
             visited.add((i, j))
             while queue:
                curr_i, curr_j = queue.popleft()
                
                for x, y in directions:
                    r, c = curr_i + x, curr_j + y
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    find_island(r, c)
                    count += 1

        return count

