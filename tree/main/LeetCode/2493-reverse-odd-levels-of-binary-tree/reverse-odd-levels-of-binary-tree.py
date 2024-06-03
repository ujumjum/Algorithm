# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level_vals = []
            nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                nodes.append(node)
                current_level_vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # reverse Odd level
            if level % 2 == 1:
                current_level_vals.reverse()
                for i, node in enumerate(nodes):
                    node.val = current_level_vals[i]
                    
            
            level+=1
        
        return root