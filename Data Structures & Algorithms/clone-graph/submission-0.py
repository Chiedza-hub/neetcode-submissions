"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        result = {}
        

        def dfs(node):
            if node in result:
                return result[node]
            
            clone = Node(node.val)
            result[node] = clone

            for nei in node.neighbors:
                clone_nei = dfs(nei)
                clone.neighbors.append(clone_nei)

            return clone

        return dfs(node)
        