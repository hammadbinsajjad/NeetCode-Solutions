from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree1 = deque()
        self.tree2 = deque()

    def dfs(self, node, tree):
        if node is None:
            if tree == 1:
                self.tree1.append(None)
            else:
                self.tree2.append(None)
            return

        if tree == 1:
            self.tree1.append(node.val)
        else:
            self.tree2.append(node.val)

        self.dfs(node.left, tree)
        self.dfs(node.right, tree)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p, 1)
        self.dfs(q, 2)

        if self.tree1 == self.tree2:
            return True
        else:
            return False
