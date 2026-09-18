

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def count_area(r, c):
            stack = [(r, c)]
            grid[r][c] = 0
            count = 1

            while stack:
                row, col = stack.pop()
                for nr, nc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                        stack.append((nr, nc))
                        grid[nr][nc] = 0
                        count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visited:
                    area = count_area(r, c)
                    max_area = max(max_area, area)
        return max_area
        