## [Problem](https://leetcode.com/problems/max-consecutive-ones-iii/submissions/)
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
```
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```
Note:
- 1 <= A.length <= 20000
- 0 <= K <= A.length
- A[i] is 0 or 1 

## My Solution
Steps:
- count the length of subarray containing only 0s and 1s.
    ```
    A = [1,1,1,0,0,0,1,1,1,1,0]
    lens = [3, 3, 4, 1]
    ```
- make every subarray containing 1s as the start. change the subarray containing 0s nearby to make the subarray containing 1s become as long as possible.
- `maxLen = Math.max(maxLen, len);`

## Easier Solution: Sliding Window
```
public int longestOnes(int[] A, int K) {
        int res = 0;
        // [start , i] is the subarray containing only 1s.
        for (int i = 0, cnt = 0, start = 0; i < A.length; i++) {
            if (A[i] == 0)
                cnt++;
            // cnt+=1-A[i];
            while (cnt > K)
                // if cnt > k, there must be 0 before i, 
                // `start` should be exactly the index of the first 0 after `start`;
                if (A[start++] == 0)
                    cnt--;
            res = Math.max(i - start + 1, res);
        }
        return res;
    }
```

