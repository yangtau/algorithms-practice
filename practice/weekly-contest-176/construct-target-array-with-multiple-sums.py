'''
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
'''
from heapq import *


class Solution:
    def isPossible(self, target: [int]) -> bool:
        '''
        To construct a list of all 1's, we need to find the max elements `m`,
        and replace it with `m-(sum-m)`. We can use heap to speed up this
        process.
        '''
        heap = [-t for t in target]
        heapify(heap)
        s = sum(target)
        while len(heap) > 0:
            t = -heap[0]
            if t == 1:
                break
            old = t - (s - t)
            s -= t - old
            if old < 1:
                return False
            heapreplace(heap, -old)
        return True

    def isPossible0(self, target: [int]) -> bool:
        '''Original solution
        We first check if every integer in `target` is valid.
        Valid integer can be denoted as: A(n) = A(n-1) + len-1, where A(0) = 1.
        Thus A(n) = n*(len-1) + 1, (A(n)-1) % (len-1) == 0.
        If all elements pass the check, we try to construct a list consisting
        of all 1's.
        '''
        s = len(target)-1
        v = set()
        for t in target:
            if t != 1 and t in v:
                return False
            if (t-1) % s != 0:
                return False
            v.add(t)
        s = sum(target)
        m = len(target)
        while True:
            max_, idx = 0, 0
            for i in range(m):
                if target[i] > max_:
                    max_ = target[i]
                    idx = i
            if max_ == 1:
                break
            t = max_-(s-max_)
            s -= max_ - t
            if t < 1:
                return False
            target[idx] = t
        return True
