# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: 
        ans = 0
        def traversal(root, ans):
            ans = 0
            if not root:
                return ans
            if root.val>=low and root.val<=high:
                ans+=root.val
            ans += traversal(root.left, ans)
            ans += traversal(root.right, ans)
            return ans
        return traversal(root, ans)
        