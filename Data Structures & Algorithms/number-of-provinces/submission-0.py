class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()
        res = 0

        def dfs(node):
            visited.add(node)
            for i in range(len(isConnected[node])):
                if isConnected[node][i] and i not in visited:
                    dfs(i)

        
        for i in range(len(isConnected[0])):
            if i not in visited:
                dfs(i)
                res += 1

        return res



        