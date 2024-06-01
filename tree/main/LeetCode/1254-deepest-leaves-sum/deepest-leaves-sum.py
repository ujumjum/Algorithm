# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = self.maxDepth(root)
        
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return 0
            if depth == max_depth:
                return node.val
            return dfs(node.left, depth + 1) + dfs(node.right, depth + 1)
        
        return dfs(root, 1)