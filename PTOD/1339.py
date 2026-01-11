# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        MOD = 10**9 +7
        self.mx = 0

        def totalSum(node):
            if not node:
                return 0
            return totalSum(node.left) + totalSum(node.right) + node.val

        total = totalSum(root)

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            curr_sum = left + right + node.val
            self.mx = max( self.mx, (total - curr_sum) * curr_sum)

            return curr_sum 

        dfs(root)
        return self.mx % MOD