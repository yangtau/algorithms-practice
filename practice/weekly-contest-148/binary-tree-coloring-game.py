# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def countSon(son: TreeNode):
    return 0 if son == None else 1+countSon(son.left)+countSon(son.right)


def findAndCount(root: TreeNode, x: int) -> (int, int):
    if root == None:
        return None
    if root.val == x:
        return countSon(root.left), countSon(root.right)
    r = findAndCount(root.left, x)
    return r if r != None else findAndCount(root.right, x)


class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        left, right = findAndCount(root, x)
        other = n - left - right - 1
        if other > left+right or left > other+right or right > other+left:
            return True
        return False
