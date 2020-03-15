# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
KMP algorithm
https://leetcode.com/problems/linked-list-in-binary-tree/submissions/
'''


class Solution:
    def kmp_table(self, t) -> [int]:
        table = [-1] * len(t)
        cnd = 0
        for pos in range(1, len(t)):
            if t[pos] == t[cnd]:
                table[pos] = table[cnd]
            else:
                table[pos] = cnd
                while cnd >= 0 and t[cnd] != t[pos]:
                    cnd = table[cnd]
            cnd += 1
        return table

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        xs = []
        while head is not None:
            xs.append(head.val)
            head = head.next

        tb = self.kmp_table(xs)

        def dfs(cur, idx):
            if cur is None:
                return False
            if cur.val == xs[idx]:
                if idx+1 == len(xs):
                    return True
            else:
                idx = tb[idx]
                while idx >= 0 and xs[idx] != cur.val:
                    idx = tb[idx]
            return dfs(cur.left, idx+1) or dfs(cur.right, idx+1)

        return dfs(root, 0)
