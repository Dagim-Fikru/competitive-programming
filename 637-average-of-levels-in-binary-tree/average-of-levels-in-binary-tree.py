# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            level = 0
            for i in range(n):
                node = queue.popleft()
                if node:
                    level+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            # print(queue,n)
            # if level:
            ans.append(level/n)
        return ans