from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def count_area(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            count = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visited:
                    area = count_area(r, c)
                    if area > max_area:
                        max_area = area
        return max_area
        