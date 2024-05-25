# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent = {}

        def findPar(node, par):
            if not node:
                return
            parent[node] = par
            findPar(node.left, node)
            findPar(node.right, node)
        
        findPar(root, None)
        
        seen = set()
        q = [target]
        step = -1
        
        while q:
            size = len(q)
            res = []
            for _ in range(size):
                node = q.pop(0)
                res.append(node.val)
                seen.add(node.val)
                if node.left and node.left.val not in seen:
                    q.append(node.left)
                    seen.add(node.left.val)
                if node.right and node.right.val not in seen:
                    q.append(node.right)
                    seen.add(node.right.val)
                if parent[node] and parent[node].val not in seen:
                    q.append(parent[node])
                    seen.add(parent[node].val)
            
            step += 1
            if step == k:
                return res
        return []
        