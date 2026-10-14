from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        regions = []
        rows, cols = len(board), len(board[0])

        def get_region(r, c):
            queue = deque([(r, c)])
            region = [(r, c)]
            seen.add((r, c))
            edge = False 
            if ( 0 == r or r == rows - 1 or 0 == c or c == cols - 1):
                edge = True
            
            while queue:
                curr_r, curr_c = queue.popleft()
                for nr, nc in [(curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1) ]:
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr, nc) not in seen:
                        if ( 0 == nr or nr == rows - 1 or 0 == nc or nc == cols - 1):
                            edge = True
                        region.append((nr, nc))
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            
            if not edge:
                regions.append(region)
            return

        # get all the regions 
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and board[r][c] == 'O':
                    get_region(r, c)
                    

        # capture all the regions
        for region in regions:
            for a, b in region:
                board[a][b] = 'X'

        return
