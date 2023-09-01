# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node, lst, lst2, depth, p, q):
        self.i += 1
        lst.append(node.val)
        lst2.append(depth)
        if node.val == p.val and self.p_ind is None:
            self.p_ind = self.i
        if node.val == q.val and self.q_ind is None:
            self.q_ind = self.i

        if node.left:
            self.dfs(node.left, lst, lst2, depth + 1, p, q)
            lst.append(node.val)
            lst2.append(depth)
            self.i += 1
        if node.right:
            self.dfs(node.right, lst, lst2, depth + 1, p, q)
            lst.append(node.val)
            lst2.append(depth)
            self.i += 1

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        traversal = []
        heights = []
        self.p_ind = None
        self.q_ind = None
        self.i = -1
        self.dfs(root, traversal, heights, 0, p, q)
        print(traversal)
        print(heights)
        print(self.p_ind)
        print(self.q_ind)
        try:
            req_traversal = traversal[self.p_ind: self.q_ind]
            req_heights = heights[self.p_ind: self.q_ind]
            mn = min(req_heights)
        except:
            req_traversal = traversal[self.q_ind: self.p_ind]
            req_heights = heights[self.q_ind: self.p_ind]
            mn = min(req_heights)
        ind = req_heights.index(mn)

        return TreeNode(req_traversal[ind])

        