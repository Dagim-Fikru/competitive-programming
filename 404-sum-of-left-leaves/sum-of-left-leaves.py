# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node:
                    if node.left:
                        if not node.left.left and not node.left.right:
                            ans+=node.left.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return ans


