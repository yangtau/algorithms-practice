import java.util.ArrayList;
import java.util.List;

class Solution {
    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public int[] nextLargerNodes(ListNode head) {
        int[] arr = new int[10001];
        int n = 0;
        for (ListNode p = head; p != null; p = p.next)
            arr[n++] = p.val;
        int[] nextLarger = new int[n];
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[i]) {
                    nextLarger[i] = arr[j];
                    break;
                } else if (arr[j] == arr[i] || nextLarger[j] == 0) {
                    nextLarger[i] = nextLarger[j];
                    break;
                }
            }
        }
        return nextLarger;
    }

    public static void main(String[] args) {

    }
}