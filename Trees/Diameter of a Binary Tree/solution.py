 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0
    def dfs(self, node):
        if node is None:
            return 0

        d1 = self.dfs(node.right)
        d2 = self.dfs(node.left)

        self.max_distance = max(self.max_distance, d1 + d2)
        return 1 + max(d1, d2)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_distance
