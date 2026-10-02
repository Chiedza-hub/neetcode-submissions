class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        def bfs(source, ocean):
            while source:
                r, c = source.popleft()
                ocean[r][c] = True
                for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (0 <= dr < rows and 0 <= dc < cols) and not ocean[dr][dc] and heights[dr][dc] >= heights[r][c]:
                        source.append((dr, dc))

        pacific = deque()
        atlantic = deque()

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        result = []
        for r in range(rows):
            for c in range(cols):
                if atl[r][c] and pac[r][c]:
                    result.append([r, c])

        return result
