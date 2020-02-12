/*
 * https://leetcode.com/problems/maximum-students-taking-exam/
 *
 */

#include <string.h>
static inline int max(int a, int b) { return a > b ? a : b; }

static inline int min(int a, int b) { return a < b ? a : b; }

/* count the number of 1 in the last n bits */
static inline int bit_count(unsigned bits, int n) {
  unsigned mask = 1;
  int res = 0;
  while (mask < (1 << n)) {
    if (mask & bits)
      res++;
    mask <<= 1;
  }
  return res;
}

int maxStudents(char **seats, int seatsSize, int *seatsColSize) {
  const int m = seatsSize, n = *seatsColSize;
  int dp[m][1 << n];
  unsigned seatmask[m];
  memset(dp, 0, sizeof(dp));
  memset(seatmask, 0, sizeof(seatmask));
  /*
   * seatmask[i] denotes the bitmask in row i.
   *
   * dp[i][mask] denotes the max students in the first i row with a `mask` in
   * row i.
   * dp[i][mask] = max(dp[i-1][ml] for ml and mask is compatible)
   *
   * For a row bitmask `mask`, `mask` should be a subset of `seatmask[row]`.
   * Say, (mask & seatmask[row]) == mask.
   * And `mask` should be self compatible. Say, (mask & (mask>>1))==0.
   *
   * For two adjacent rows: `mask`, `ml`, they are compatible only if:
   * (mask & (ml>>1))==0 and ((mask>>1) & ml)==0
   *
   * Why is it different for the two kinds of compatibility?
   * For a four-seats row, using `abcd` to denote every bit, if it is self
   * compatible, then a&b, c&b, d&c should be 0.
   * abcd
   *  abcd
   * But for two rows: `abcd`, `efgh`, it should be a&f, b&e, b&g, c&f, c&h, d&g to be 0
   * abcd       abcd
   *  efgh     efgh
   */

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (seats[i][j] == '.') {
        seatmask[i] |= 1 << j;
      }
    }
  }

  for (int row = 0; row < m; row++) {
    for (unsigned mask = 0; mask < (1 << n); mask++) {
      if ((mask & seatmask[row]) == mask && (mask & (mask >> 1)) == 0) {
        int bitcnt = bit_count(mask, n);
        dp[row][mask] = bitcnt;
        if (row == 0)
          continue;
        for (unsigned lm = 0; lm < (1 << n); lm++) {
          if ((lm & seatmask[row - 1]) != lm || (lm & (lm >> 1)) != 0 ||
              dp[row - 1][lm] == 0 || (lm & (mask >> 1)) != 0 ||
              ((lm >> 1) & mask) != 0)
            continue;
          dp[row][mask] = max(dp[row - 1][lm] + bitcnt, dp[row][mask]);
        }
      }
    }
  }

  int res = 0;
  for (unsigned mask = 0; mask < (1 << n); mask++) {
    res = max(res, dp[m - 1][mask]);
  }
  return res;
}

#if 1
#include <stdio.h>

int main() {
  {
    char s1[] = {'#', '.', '#', '#', '.', '#'};
    char s2[] = {'.', '#', '#', '#', '#', '.'};
    char s3[] = {'#', '.', '#', '#', '.', '#'};
    char *seats[] = {s1, s2, s3};

    int cols[] = {6, 6, 6};

    int res = maxStudents(seats, 3, cols);

    printf("%d\n", res);
  }
  {
    char s1[] = {'.', '#'};
    char s2[] = {'#', '#'};
    char s3[] = {'#', '.'};
    char s4[] = {'#', '#'};
    char s5[] = {'.', '#'};
    char *seats[] = {s1, s2, s3, s4, s5};
    int cols[] = {2};

    int res = maxStudents(seats, 5, cols);
    printf("%d\n", res);
  }
  {

    char s1[] = {'.', '#', '#', '.'};
    char s2[] = {'.', '.', '.', '#'};
    char s3[] = {'.', '.', '.', '.'};
    char s4[] = {'#', '.', '#', '#'};
    char *seats[] = {s1, s2, s3, s4};
    int cols[] = {4};

    int res = maxStudents(seats, 4, cols);
    printf("%d\n", res);
  }
  return 0;
}
#endif
