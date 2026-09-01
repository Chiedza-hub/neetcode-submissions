# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def subtreeheight(node):
            if not node:
                return 0
            return 1 + max(subtreeheight(node.left), subtreeheight(node.right))

        if not root:
            return 0
        
        max_num = 0
        stack = [(root)]

        while stack:
            curr = stack.pop()
            left_h = subtreeheight(curr.left)
            right_h = subtreeheight(curr.right)
            curr_h = left_h + right_h

            if curr_h > max_num:
                max_num = curr_h
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return max_num
        