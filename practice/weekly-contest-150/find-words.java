class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] charsCnt = new int[26];
        int len = 0;
        for (char c : chars.toCharArray())
            charsCnt[(int) (c - 'a')]++;
        for (String word : words) {
            int[] wordCnt = new int[26];
            for (char c : word.toCharArray()) {
                wordCnt[(int) (c - 'a')]++;
            }
            int i = 0;
            for (; i < 26; i++) {
                if (wordCnt[i] > charsCnt[i]) {
                    break;
                }
            }
            if (i == 26)
                len += word.length();
        }
        return len;
    }

    public static void main(String[] args) {
        String[] words = { "cat", "bt", "hat", "tree" };
        String chars = "atach";
        System.out.println(new Solution().countCharacters(words, chars));
    }
}