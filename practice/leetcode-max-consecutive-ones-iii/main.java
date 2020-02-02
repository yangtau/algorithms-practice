import java.util.Arrays;

class Solution {

    private int mysolve(int[] A, int K) {
        int[] lens = new int[A.length];
        int n = 0;
        for (int i = 0, cnt = 0, pre = (A[0] == 0 ? 1 : 0); i < A.length; i++) {
            if (A[i] == pre)
                cnt++;
            else {
                lens[n++] = cnt;
                cnt = 1;
                pre = A[i];
            }
            if (i == A.length - 1) {
                lens[n++] = cnt;
            }
        }
        int maxLen = 0;
        System.out.println(Arrays.toString(lens));
        for (int i = (A[0] == 0 ? 2 : 1); i < n; i += 2) {
            // i is the start of the subarray
            int len = lens[i];
            int cnt = 0;
            int j = i + 1;
            // change the subarray containing 0s afer i
            while (j < n && cnt + lens[j] <= K) {
                len += lens[j] + (j + 1 < n ? lens[j + 1] : 0);
                cnt += lens[j];
                j += 2;
            }
            if (j < n) {
                // cnt + lens[j] <= K must be false,
                // thereby the ramaining chance to change 0 to 1 is not enough to make j all 1.
                len += K - cnt;
            } else {
                len += (K - cnt >= lens[i - 1] ? lens[i - 1] : K - cnt);
            }
            System.out.println(len);
            maxLen = Math.max(maxLen, len);
        }
        return maxLen;
    }

    public int longestOnes(int[] A, int K) {
        int res = 0;
        for (int i = 0, cnt = 0, start = 0; i < A.length; i++) {
            if (A[i] == 0)
                cnt++;
            // cnt+=1-A[i];
            while (cnt > K)
                if (A[start++] == 0)
                    cnt--;
            res = Math.max(i - start + 1, res);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] a = { 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 };
        int res = solution.longestOnes(a, 2);
        System.out.println(res);
    }
}