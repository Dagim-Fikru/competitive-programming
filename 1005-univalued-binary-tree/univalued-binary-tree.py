# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        newRoot = root.val
        def dfs(node):
            if not node:
                return True
            elif node.val!=newRoot:
                return False
            else:
                return dfs(node.left) and dfs(node.right)
        return dfs(root)