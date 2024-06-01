# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # BFS
        queue = [root]

        while queue:
            leaves_sum = 0
            # 현재 level node 수
            level_size = len(queue)

            # 현재 level node 처리
            for _ in range(level_size):
                node = queue.pop(0)
                leaves_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leaves_sum