class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[-1] * n for _ in range(m)]
       
        def dfs(a, b):
        
            if a == m - 1 and b == n - 1:
                return 1
            if a >= m or b >= n: # out of bounds
                return 0
            if mem[a][b] != -1:
                return mem[a][b]
            mem[a][b] = dfs(a, b + 1) + dfs(a + 1, b)
            return mem[a][b]
        
        return dfs(0, 0)
        

