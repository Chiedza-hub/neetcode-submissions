# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def are_equal(root_node, subtree_node):
            if not root_node and not subtree_node:
                return True
            if not root_node or not subtree_node:
                return False
            return (root_node.val == subtree_node.val and  are_equal(root_node.left, subtree_node.left) and are_equal(root_node.right, subtree_node.right))
            
        if not root:
            return False
        if are_equal(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))




        

        