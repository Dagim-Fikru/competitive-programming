# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delete(node):
            if not node:
                return False
            left_deleted = delete(node.left)
            right_deleted = delete(node.right)
            if node.val in to_delete:
                if not left_deleted and node.left:
                    ans.append(node.left)
                if not right_deleted and node.right:
                    ans.append(node.right)
                return True
            if left_deleted:
                node.left = None
            if right_deleted:
                node.right = None
            return False
        
        to_delete = set(to_delete)
        ans = []
        if not delete(root):
            ans.append(root)
        return ans