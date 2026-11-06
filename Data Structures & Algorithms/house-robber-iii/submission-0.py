# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mem = {} # node : total

        def rob_grandchildren(node):
            grand1, grand2, grand3, grand4 = 0, 0, 0, 0

            if node.left:
                grand1 = rob_rec(node.left.left)
                grand2 = rob_rec(node.left.right)
            if node.right:
                grand3 = rob_rec(node.right.left)
                grand4 = rob_rec(node.right.right)
            
            return grand1 + grand2 + grand3 + grand4


        def rob_rec(node):
            if not node:
                return 0
            if node in mem:
                return mem[node]
            
            # rob it 
            rob = node.val + rob_grandchildren(node)
            # not rob it 
            skip = rob_rec(node.left) + rob_rec(node.right)
            mem[node] = max(rob, skip)

            return mem[node]

        return rob_rec(root)

        