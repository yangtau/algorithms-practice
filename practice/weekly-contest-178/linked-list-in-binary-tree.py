'''
https://leetcode.com/problems/linked-list-in-binary-tree/
TODO: use KMP alg to solve it
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def is_sub_path(r, h):
            if h is None:
                return True
            if r is None or r.val != h.val:
                return False
            return is_sub_path(r.left, h.next) or is_sub_path(r.right, h.next)

        def visit(tree):
            if is_sub_path(tree, head):
                return True
            if tree is not None:
                return visit(tree.left) or visit(tree.right)
            return False
        return visit(root)
