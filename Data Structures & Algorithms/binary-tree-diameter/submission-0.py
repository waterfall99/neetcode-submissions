# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0
        def finding_max(node):
            if node is None:
                return 0
            left_count = finding_max(node.left)
            right_count = finding_max(node.right)
            self.global_max = max(self.global_max, (left_count + right_count))
            return max(left_count, right_count) + 1
        temp_count = finding_max(root)
        return self.global_max