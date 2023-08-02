# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balanced = True

    def dfs(self, node, depth):
        if node is None:
            return depth

        d1 = self.dfs(node.left, depth + 1)
        d2 = self.dfs(node.right, depth + 1)

        if abs(d1 - d2) > 1:
            self.balanced = False

        return max(d1, d2)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root, 0)
        return self.balanced
