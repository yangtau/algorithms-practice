from collections import defaultdict


class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:
        m = len(light) + 1
        on = [False]*m
        blue = [False]*m
        i = 0
        res = 0
        while i < m-1:
            l = light[i]
            on[l] = True
            if l == 1 or blue[l-1]:
                blue[l] = True
                j = l+1
                while j < m and on[j]:
                    blue[j] = True
                    j += 1
                # print("on:   ", on[1:])
                # print("blue: ", blue[1:])
                if on == blue:
                    res += 1
            i += 1
        return res

    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        dp = [0] * n

        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            if i == headID:
                dp[i] = informTime[i]
            else:
                dp[i] = informTime[i] + dfs(manager[i])
            return dp[i]
        m = 0
        for i in range(n):
            m = max(dfs(i), m)
        return m

    def frogPosition(self, n: int, edges, t: int, target: int):
        g = defaultdict(list)
        for f, nxt in edges:
            g[f].append(nxt)
            g[nxt].append(f)

        def dfs(pos, possi, time, prev):
            if pos == target:
                return possi
            if time == 0:
                return 0
            for nxt in g[pos]:
                if nxt == prev:
                    continue
                # print(pos, g[pos])
                tmp = possi * 1/(len(g[pos])-1 if prev != 0 else len(g[pos]))
                re = dfs(nxt, tmp, time-1, pos)
                if re != 0:
                    return re
            return 0
        return dfs(1, 1, t, 0)


n = 7
edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
t = 2
target = 4
s = Solution()
print(s.frogPosition(n, edges, t, target))

t = 1
target = 7

print(s.frogPosition(n, edges, t, target))
t = 20
target = 6
print(s.frogPosition(n, edges, t, target))

n = 3
edges = [[2, 1], [3, 2]]
t = 1
target = 2
print(s.frogPosition(n, edges, t, target))
