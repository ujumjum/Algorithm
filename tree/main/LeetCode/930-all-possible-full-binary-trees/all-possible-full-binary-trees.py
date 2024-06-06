# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # n이 짝수인 경우
        if n % 2 == 0:  
            return []

        # 메모이제이션을 위한 dictionary
        memo = {}  

        def allPossibleFBTInner(n):
            if n == 1:  # n이 1인 경우
                return [TreeNode(0)]

            if n in memo:  # 이미 계산된 결과가 있는 경우
                return memo[n]

            result = []

            for left_tree_size in range(1, n, 2):
                right_tree_size = n - 1 - left_tree_size
                for left in allPossibleFBTInner(left_tree_size):
                    for right in allPossibleFBTInner(right_tree_size):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[n] = result  # 결과를 메모이제이션에 저장
            return result

        return allPossibleFBTInner(n)