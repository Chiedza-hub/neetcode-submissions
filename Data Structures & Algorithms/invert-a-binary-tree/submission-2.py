# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''if not root:
            return None
        
        def swap(head, l, r):
            if not head:
                return
            if l:
                swap(l, l.left, l.right)
            if r:
                swap(r, r.left, r.right)

            head.left = r
            head.right = l
        
        swap(root, root.left, root.right)

        return root
        '''


        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
