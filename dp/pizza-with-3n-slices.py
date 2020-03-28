from functools import lru_cache

'''
https://leetcode.com/problems/pizza-with-3n-slices/submissions/
'''


class Solution:
    def maxSizeSlices(self, slices: [int]) -> int:
        m = len(slices)
        @lru_cache(None)
        def dp(i, j, k):
            print(i, j, k)
            if j-i < 2*k-1 or k == 0:
                return -float('inf')
            if k == 1:
                return max(slices[i:j])
            return max(dp(i, j-2, k-1)+slices[j-1], dp(i, j-1, k))
        return max(dp(0, m-1, m//3), dp(1, m-2, m//3-1) + slices[m-1])
