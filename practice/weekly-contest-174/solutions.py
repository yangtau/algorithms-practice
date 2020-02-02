from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        res = []
        for i, row in enumerate(mat):
            res.append((sum(1 for j in row if j == 1), i))
        res.sort()
        return [res[j][1] for j in range(k)]

    def minSetSize(self, arr: [int]) -> int:
        d = defaultdict(int)
        for a in arr:
            d[a] += 1
        cnts = sorted([v for k, v in d.items()], reverse=True)
        res, acc = 0, 0
        for c in cnts:
            acc += c
            res += 1
            if acc >= len(arr)/2:
                break
        return res

    def maxProduct(self, root: TreeNode) -> int:
        sums = []

        def sumTree(tree: TreeNode):
            if tree is None:
                return 0
            res = sumTree(tree.left) + sumTree(tree.right) + tree.val
            sums.append(res)
            return res
        half = sumTree(root) / 2
        close = sums[0]
        for i in sums:
            if abs(close-half) > abs(i-half):
                close = i
        return close * (sum[-1] - close)

    def maxJumps(self, arr: [int], d: int) -> int:
        memo = [0 for _ in range(len(arr))]

        def dp(i):
            if memo[i] != 0:
                return memo[i]
            memo[i] = 1
            for j in range(i+1, min(i+d+1, len(arr))):
                if arr[j] >= arr[i]:
                    break
                memo[i] = max(memo[i], 1+dp(j))
            for j in range(i-1, max(0, i-d-1), -1):
                if arr[j] >= arr[i]:
                    break
                memo[i] = max(memo[i], 1+dp(j))
            return memo[i]
        return max(dp(i) for i in range(len(arr)))
