from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # get all the rotten fruits and fresh fruit count
        
        fresh = 0
        minute = 0
        queue = deque()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r, c))
        
        while queue and fresh:
            for i in range(len(queue)):
                nr, nc = queue.popleft()

                for x, y in [(nr, nc + 1), (nr, nc - 1), (nr + 1, nc), (nr - 1, nc)]:
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and (x, y) not in seen:
                        grid[x][y] = 2
                        fresh -= 1
                        queue.append((x, y))
                        seen.add((x, y))
            minute += 1

        return minute if not fresh else -1




        