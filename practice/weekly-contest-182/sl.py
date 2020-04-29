from collections import defaultdict
from functools import lru_cache


class Solution:
    def findLucky(self, arr: [int]) -> int:
        cnt = defaultdict(int)
        for x in arr:
            cnt[x] += 1
        return max((k if k == v else -1) for k, v in cnt.items())

    def numTeams(self, rating: [int]) -> int:
        m = len(rating)
        res = 0
        for i in range(m):
            for j in range(i+1, m):
                for k in range(j+1, m):
                    if rating[i] < rating[j] < rating[k]:
                        res += 1
                    if rating[i] > rating[j] > rating[k]:
                        res += 1
        return res

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def kmp(t):
            tb, j = [-1]*len(t), 1
            for i in range(1, len(t)):
                tb[i] = tb[j] if t[i] == t[j] else j
                while j >= 0 and t[j] != t[i]:
                    j = tb[j]
                j += 1
            return tb

        fail = kmp(evil)
        @lru_cache(None)
        def dfs(idx, pre1, pre2, max_match):
            if max_match == len(evil): return 0
            if idx == n: return 1
            c1 = s1[idx] if pre1 else 'a'
            c2 = s2[idx] if pre2 else 'z'
            s = 0
            for i in range(ord(c1), ord(c2)+1, 1):
                c, match = chr(i), max_match
                while match != -1 and c != evil[match]:
                    match = fail[match]
                s += dfs(idx+1, pre1 and c==s1[idx], pre2 and c==s2[idx], match+1)
            return s % (10**9+7)
        return dfs(0, True, True, 0)


class UndergroundSystem:
    # Your UndergroundSystem object will be instantiated and called as such:
    # obj = UndergroundSystem()
    # obj.checkIn(id,stationName,t)
    # obj.checkOut(id,stationName,t)
    # param_3 = obj.getAverageTime(startStation,endStation)
    def __init__(self):
        self.ins = defaultdict(dict)
        self.outs = defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        d = self.ins
        d[stationName][id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        d = self.outs
        d[stationName][id] = t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s, n = 0, 0
        for id, st in self.ins[startStation].items():
            if endStation in self.outs and id in self.outs[endStation]:
                end = self.outs[endStation][id]
                s += end - st
                n += 1
        return s/n
