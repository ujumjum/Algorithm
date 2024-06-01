from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])  # deque로 큐를 초기화합니다.
        leaves_sum = 0

        while queue:
            level_size = len(queue)
            leaves_sum = 0

            for _ in range(level_size):
                node = queue.popleft()  # pop(0) 대신 popleft()를 사용합니다.
                leaves_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leaves_sum
