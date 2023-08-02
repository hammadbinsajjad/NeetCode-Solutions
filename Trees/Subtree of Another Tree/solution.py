 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, tree1, tree2):
        if tree1 is None and tree2 is not None:
            return False
        if tree1 is not None and tree2 is None:
            return False
        if tree1 is None and tree2 is None:
            return True

        return tree1.val == tree2.val and \
            self.sameTree(tree1.right, tree2.right) and \
            self.sameTree(tree1.left, tree2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return True

        return self.sameTree(root, subRoot) or \
                self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)


