import math


class Solution:
    def mctFromLeafValues(self, arr: [int]) -> int:
        return self.dp_solution(arr)

    def dp_solution(self, arr: [int]) -> int:
        m = len(arr)
        max_memo = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            max_memo[i][i] = arr[i]
            for j in range(i+1, m):
                max_memo[i][j] = max(max_memo[i][j-1], arr[j])
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for l in range(2, m+1):
            for left in range(m+1-l):
                right = left+l-1
                dp[left][right] = math.inf
                for j in range(left, right):
                    dp[left][right] = min(
                        dp[left][right], dp[left][j]+dp[j+1][right] +
                        max_memo[left][j]*max_memo[j+1][right])

        return dp[0][m-1]

    def greedy_solution(self, arr: [int]) -> int:
        stack = [math.inf]
        res = 0
        for i in arr:
            if i > stack[-1]:
                res += stack.pop(-1) * min(stack[-1], i)
            stack.append(i)
        while len(stack) >= 2:
            res += stack.pop(-1) * stack.pop(-1)
        return res
