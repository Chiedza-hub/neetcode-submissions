import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) # square grid
        visited = set()
        minH = [[grid[0][0], 0, 0]] # height/max, r, c
        visited.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in [(r, c + 1), (r + 1, c), (r - 1, c), (r, c - 1)]:
                if 0 <= dr < N and 0 <= dc < N and (dr, dc) not in visited:
                    heapq.heappush(minH, [max(t, grid[dr][dc]), dr, dc])
                    visited.add((dr, dc))
        

                    
            
            


        
       
