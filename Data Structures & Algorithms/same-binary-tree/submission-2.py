# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(node, node2):
            if node is None and node2 is None:
                return True
            elif node is None:
                return False
            elif node2 is None:
                return False
            if node.val != node2.val:
                return False
            return checkTree(node.left, node2.left) and checkTree(node.right, node2.right)
        return checkTree(p, q)



        