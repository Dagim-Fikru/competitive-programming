# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root
        q = root
        def check(p,q):
            if p==None and q==None:
                return True
            if p==None or q==None:
                return False
            if p.val==q.val:
                return check(q.left,p.right) and check(q.right,p.left)
            return False
        return check(p,q)