import queue
from collections import defaultdict


class UF:
    def __init__(self, n):
        self.xs = [i for i in range(n)]

    def find(self, x):
        if x != self.xs[x]:
            self.xs[x] = self.find(self.xs[x])
        return self.xs[x]

    def union(self, x, y):
        self.xs[self.find(x)] = self.find(y)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
        uf = UF(len(s))
        for x, y in pairs:
            uf.union(x, y)
        d = defaultdict(queue.PriorityQueue)
        for i in range(len(s)):
            d[uf.find(i)].put(s[i])
        xs = [d[uf.find(i)].get() for i in range(len(s))]
        return ''.join(xs)

def test1():
    s = "udyyek"
    pairs = [[3, 3], [3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]

    sl = Solution()
    print(sl.smallestStringWithSwaps(s, pairs))


test1()
