'''
https://leetcode.com/problems/maximum-performance-of-a-team/
'''
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: [int], effi: [int], k: int) -> int:
        h = []
        res = 0
        su = 0
        for e, s in sorted(zip(effi, speed), reverse=True):
            heapq.heappush(h, s)
            su += s
            if len(h) > k:
                su -= heapq.heappop(h)
            res = max(res, e*su)
        return res % (10**9 + 7)
