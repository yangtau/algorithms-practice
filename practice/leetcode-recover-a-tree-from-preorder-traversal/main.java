import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode recoverFromPreorder(String S) {
        return build(S.toCharArray(), 0);
    }

    private int start = 0;

    private TreeNode build(char[] tree, int height) {
        int h = 0;
        while (start + h < tree.length && tree[start + h] == '-')
            h++;
        if (h != height)
            return null;
        int val = 0;
        start += h;
        while (start < tree.length && tree[start] != '-') {
            val = val * 10 + Character.getNumericValue(tree[start++]);
        }
        TreeNode root = new TreeNode(val);
        root.left = build(tree, height + 1);
        root.right = build(tree, height + 1);
        return root;
    }
    public static void main(String[] args) {
        new Solution().recoverFromPreorder("1-2--3--4-5--6--7");
    }
}