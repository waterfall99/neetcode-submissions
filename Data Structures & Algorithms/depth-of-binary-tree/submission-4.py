# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def goingdown(node, current_depth):
            if node is None:
                return
            current_depth += 1
            goingdown(node.left, current_depth)
            goingdown(node.right, current_depth)
            self.depth = max(self.depth, current_depth)
            return
        goingdown(root, 0)
        return self.depth