from heapq import *

'''
# Greedy
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
For each day, choose the event that ends sooner.
Time: O(N*log(N))
'''


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        num = len(events)
        cnt, day = 0, 1

        # priority queue by event[1], that keeps event for event[0] <= `day`.
        # Note that event[1] may be less then `day`.
        heap = []
        i = 0
        while i < num or len(heap) > 0:
            while i < num and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1
            while len(heap) > 0:
                # pop if event[i] >= day
                if heappop(heap) >= day:
                    cnt += 1
                    break
            day += 1
        return cnt
