## [Problem](https://leetcode.com/problems/next-greater-node-in-linked-list/)

We are given a linked list with head as the first node.  Let's number the nodes in the list: `node_1, node_2, node_3`, ... etc.

Each node may have a next larger value: for `node_i`, `next_larger(node_i)` is the `node_j.val` such that` j > i, node_j.val > node_i.val`, and `j` is the smallest possible choice.  If such a `j` does not exist, the next larger value is `0`.

Return an array of integers answer, where `answer[i] = next_larger(node_{i+1})`.

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

**Example 1:**
```
Input: [2,1,5]
Output: [5,5,0]
```
**Note:**

`1 <= node.val <= 10^9` for each node in the linked list.
The given list has length in the range `[0, 10000]`.

## Solution

First, we store the LinkedList in a ArrayList `arr`, thus we get the size of the list and we can access elements in a reversed order.

Let `nextLarger` be the result, `N` is the size of the list. 

Clearly, `nextLarger[N-1]=0`.

When we find the result of `nextLarger[i]`, assume that we have found all `nextLarger[j]` where `j>i`.

Let `j=i+1`.
If `arr[j]>arr[i]`, clearly `nextLarger[i]=arr[j]`.
Else if `arr[j]==arr[i]`, than `nextLarger[i]=nextLarger[j]`.
Else if `arr[j]<arr[i]`, we need to find the answer after `j`. But there is a special situation: `nextLarger[j]==0`, which means there is no element larger than `arr[j]` in the list after `j`. And `arr[j]<arr[i]`, thus `nextLarger[i]=0`.

```java
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
```

