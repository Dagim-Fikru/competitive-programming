# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def transverse(node):
            if not node:
                return arr
            arr.append(node.val)
            transverse(node.left)
            transverse(node.right)
        transverse(root)
        arr.sort()
        return arr[k-1]
