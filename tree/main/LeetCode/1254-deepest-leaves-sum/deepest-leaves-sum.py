# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. deepest depth 구하기
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # 2. deepest leaf 노드들 값 더하기
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = self.maxDepth(root)
        
        # DFS
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return 0
            
            # deepest depth의 leafnode
            if depth == max_depth:
                return node.val
            
            # recursion
            return dfs(node.left, depth + 1) + dfs(node.right, depth + 1)
        
        # 루트부터 가장 깊은곳까지
        return dfs(root, 1)