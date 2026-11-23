# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertChildNodes(node):
            if node is None:
                return
            original_left = node.left
            node.left = node.right
            node.right = original_left
            node.left = invertChildNodes(node.left)
            node.right = invertChildNodes(node.right)
            return node
        return invertChildNodes(root)