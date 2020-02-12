class Solution {
  /*
   * https://leetcode.com/problems/minimum-falling-path-sum/
   *
   * The path passes A[i][j] is either from A[i-1][j-1] or A[i-1][j+1]. We can
   * use dp[i][j] to denote the minimum sum whose path ends at A[i][j]. Then we
   * get the transition function: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]).
   *
   */
  public int minFallingPathSum(int[][] A) {
    int len = A.length;
    int[][] dp = new int[len][len];
    for (int i = 0; i < len; i++) {
      dp[0][i] = A[0][i];
    }

    for (int i = 1; i < len; i++) {
      for (int j = 0; j < len; j++) {
        int min = dp[i - 1][j];
        if (j > 0)
          min = Math.min(dp[i - 1][j - 1], min);
        if (j < len - 1)
          min = Math.min(dp[i - 1][j + 1], min);
        dp[i][j] = A[i][j] + min;
      }
    }

    int res = 1000 * len;
    for (int i = 0; i < len; i++) {
      res = Math.min(res, dp[len - 1][i]);
    }
    return res;
  }

  public static void main(String[] args) {

  }
}
