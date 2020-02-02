class Solution {

    public int tribonacci(int n) {
        int a0 = 0, a1 = 1, a2 = 1;
        if (n == 0)
            return 0;
        for (int i = 3; i <= n; i++) {
            int t = a2;
            a2 = a2 + a1 + a0;
            a0 = a1;
            a1 = t;
        }
        return a2;
    }

    private String move(char a, char b) {
        int xa = (a - 'a') / 5, ya = (a - 'a') % 5;
        int xb = (b - 'a') / 5, yb = (b - 'a') % 5;
        StringBuffer sb = new StringBuffer();
        if (b == 'z') {
            while (ya > yb) {
                sb.append('L');
                ya--;
            }
        }
        while (xa > xb) {
            sb.append('U');
            xa--;
        }
        while (xa < xb) {
            sb.append('D');
            xa++;
        }
        while (ya > yb) {
            sb.append('L');
            ya--;
        }
        while (ya < yb) {
            sb.append('R');
            ya++;
        }
        sb.append('!');
        return sb.toString();
    }

    public String alphabetBoardPath(String target) {
        // board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        char pre = 'a';
        StringBuffer sb = new StringBuffer();
        for (char c : target.toCharArray()) {
            sb.append(move(pre, c));
            pre = c;
        }
        return sb.toString();
    }

    private boolean checkBorder(int[][] grid, int x, int y, int len) {
        for (int i = 0; i < len; i++)
            if (grid[i + x][y] == 0 || grid[i + x][y + len - 1] == 0 || grid[x][i + y] == 0
                    || grid[x + len - 1][i + y] == 0)
                return false;
        return true;
    }

    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int maxLength = Math.max(m, n);
        for (; maxLength > 0; maxLength--) {
            boolean flag = false;
            for (int i = 0; i < m; i++) {
                if (i + maxLength > m || flag)
                    break;
                for (int j = 0; j < n; j++) {
                    if (j + maxLength > n)
                        break;
                    if (checkBorder(grid, i, j, maxLength)) {
                        flag = true;
                        break;
                    }
                }
            }
            if (flag)
                break;
        }
        return maxLength * maxLength;
    }

    int dp[][];
    int sum[];
    int len;

    private int dfs(int k, int M) {
        if (dp[k][M] != 0)
            return dp[k][M];
        if (k + 2 * M >= len) {
            dp[k][M] = sum[len] - sum[k];
            return dp[k][M];
        }
        int min = 10000000;
        for (int i = 1; i <= M * 2; i++) {
            min = Math.min(min, dfs(k + i, Math.max(M, i)));
        }
        dp[k][M] = sum[len] - sum[k] - min;
        return dp[k][M];
    }

    public int stoneGameII(int[] piles) {
        len = piles.length;
        dp = new int[len][len];
        sum = new int[len + 1];
        for (int i = 0; i < len; i++) {
            sum[i + 1] = sum[i] + piles[i];
        }
        return dfs(0, 1);
    }

    public static void main(String[] args) {
        var sl = new Solution();
        int[] piles = { 2, 7, 9, 4, 4 };
        System.out.println(sl.stoneGameII(piles));
    }
}