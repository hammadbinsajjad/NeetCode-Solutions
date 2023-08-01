from copy import deepcopy
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = deepcopy(root)
        self.dfs(root, tree)
        return tree

    def dfs(self, tree1, tree2):
        if tree1 is None or tree2 is None:
            tree2 = None
            return

        tree2.val = tree1.val

        if tree1.right is not None:
            tree2.left = TreeNode()
            self.dfs(tree1.right, tree2.left)
        else:
            tree2.left = None
            
        if tree1.left is not None:
            tree2.right = TreeNode()
            self.dfs(tree1.left, tree2.right)
        else:
            tree2.right = None
