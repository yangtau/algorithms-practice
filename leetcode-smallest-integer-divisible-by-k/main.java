class Solution {

    public int smallestRepunitDivByK(int K) {
        if (K % 10 == 5 || K % 2 == 0)
            return -1;
        int cur = 1, len = 1;
        while (true) {
            if (cur % K == 0)
                return len;
            cur = (cur * 10 + 1) % K;
            len++;
        }
        // return -1;
    }

    public int smallestRepunitDivByK_1(int K) {
        // if `K` ends with 5 or `K` is even, there will never be an answer.
        if (K % 10 == 5 || K % 2 == 0)
            return -1;
        // flag is redundant for x multiply a digit in `3, 5, 7, 9` can get every digit
        // in 0...10
        // boolean flag = false;
        int cnt = 0, carry = 0;
        while (true) {
            // flag = false;
            for (int i = 0; i < 10; i++) {
                if ((i * K + carry) % 10 == 1) {
                    // flag = true;
                    carry = (i * K + carry) / 10;
                    cnt++;
                    break;
                }
            }
            if (carry == 0)
                break;
            // if (!flag || carry == 0)
            // break;
        }
        // if (flag)
        return cnt;
        // else
        // return -1;
    }

    public static void main(String[] args) {
        int[] arr = { 2, 2, 2 };
        var res = new Solution().smallestRepunitDivByK_1(1051);
        System.out.println(res);
    }
}