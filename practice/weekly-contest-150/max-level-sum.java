import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    ArrayList<Integer> sums = new ArrayList<>();

    public void sumLevel(TreeNode cur, int height) {
        if (cur == null)
            return;
        if (sums.size() <= height)
            sums.add(cur.val);
        else
            sums.set(height, sums.get(height) + cur.val);
        sumLevel(cur.left, height + 1);
        sumLevel(cur.right, height + 1);
    }

    public int maxLevelSum(TreeNode root) {
        sumLevel(root, 0);
        int maxLevel = 0;
        for (int i = 0; i < sums.size(); i++) {
            if (sums.get(i) > sums.get(maxLevel))
                maxLevel = i;
        }
        return maxLevel;
    }

    public int maxLevelSum2(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);
        int maxSum = root.val;
        int maxLevel = 0;
        for (int level = 1; !que.isEmpty(); level++) {
            // level travel
            // when initialize `i`, it just contains one level
            int levelSum = 0;
            for (int i = que.size(); i > 0; i--) {
                TreeNode top = que.poll();
                if (top.right != null)
                    que.offer(top.right);
                if (top.left != null)
                    que.offer(top.left);
                levelSum += top.val;
            }
            if (levelSum > maxSum) {
                maxSum = levelSum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }

    public static void main(String[] args) {
    }
}