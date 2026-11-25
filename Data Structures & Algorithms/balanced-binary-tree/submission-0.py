# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def checkHeight(node):
            if node is None:
                return 0
            left_height = checkHeight(node.left)
            right_height = checkHeight(node.right)
            if abs(left_height - right_height) > 1:
                self.is_balanced = False
            return 1 + max(left_height, right_height)
        checkHeight(root)
        return self.is_balanced