static inline int min(a, b) { return a > b ? b : a; }

static inline int max(a, b) { return a < b ? b : a; }
/*
 * https://leetcode.com/problems/minimum-falling-path-sum-ii/
 *
 * dp[i][j] denotes the minimum sum that the paths ends at (i, j).
 * Thus, dp[i][j] = arr[i][j] + min(dp[i-1][k] for k!=j).
 *
 * To get dp[i][j], we need to find the smallest dp[i-1][k] for `k` does not
 * equals `j`.  If we do this for every `j`, the cost is expensive(O(n^3)). We
 * can find the smallest two elements in previous row - `m1` and `m2` indicate
 * the first minimum element and the second minimum element respectively. The
 * result of min(dp[i-1][k] for k!=j) is either `m1` or `m2`. More formally,
 *          min(dp[i-1][k] for k!=j) = m1 if dp[i-1][j]!=m1 else m2.
 */
int minFallingPathSum(int **arr, int arrSize, int *arrColSize) {
  int m = arrSize, n = *arrColSize;
  if (m == 1)
    return arr[0][0];
  int dp[m + 1][n];

  int min1 = 0, min2 = 0;
  for (int i = 1; i <= m; i++) {
    int m1 = 20000000, m2 = 20000000;
    for (int j = 0; j < n; j++) {
      dp[i][j] = arr[i - 1][j] + (dp[i - 1][j] == min1 ? min2 : min1);
      if (dp[i][j] < m1)
        m2 = m1, m1 = dp[i][j];
      else
        m2 = min(m2, dp[i][j]);
    }
    min1 = m1, min2 = m2;
  }

  return min1;
}
