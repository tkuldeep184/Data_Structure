# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root):
        if not root:
            return None
        l = self.height(root.left)
        r = self.height(root.right)

        if(l == r):
            return root
        elif(l > r):
            node = self.subtreeWithAllDeepest(root.left)
        else:
            node = self.subtreeWithAllDeepest(root.right)
        return node

    def height(self, root):
            if not root:
                return 0

            l = self.height(root.left)
            r = self.height(root.right)

            return max(l,r) + 1