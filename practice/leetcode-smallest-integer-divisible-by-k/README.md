## [Problem](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

**Example 1:**

```
Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
```

**Note:**

- 1 <= K <= 10^5

## My Solution

We need to find the smallest `N` such that `N % K == 0 && N only contains digit 1`. We can find the smallest positive integer `x`, such that `x * K == N`.

Think about how we calculate multiplication by hand. For example `17 * 31`, first we calculate `17*1=17`, then `17*3=51`, the result is `17+51*10=527`.

We can just use the method how we calculate multiplication by hand. What we should do is to find the `x`, such that `N * x == 1....1`. But we don't really need to find the `x`, we just choose every digit of it to make the result of the multiplication ending with `1`.

`K * x + carry = y`, `0 <= x < 10`, and the last digit of `y` is 1. At start, `carry` is 0, and in the end of the loop we update `carry = y / 10`. When the `carry==0`, we just break from the loop.

For example, `N = 7`:

1. `carry = 0, cnt = 0`
let `x=3`, so `N*x+carry=21`, `cnt=1`, update `carry` to `21/10=2`.

2. `carry = 2, cnt = 1`
let `x=7`, so `N*x+carry=51`, `cnt=2`, `carry=5`

3. `carry = 5, cnt = 2`
let `x=8`, so `N*x+carry=61`, `cnt=3`, `carry=6`

4. `carry = 6, cnt = 3`
let `x=5`, so `N*x+carry=41`, `cnt=4`, `carry=4`

5. `carry = 4, cnt = 4`
let `x=1`, so `N*x+carry=11`, `cnt=5`, `carry=1`

6. `carry = 1, cnt = 5`
let `x=0`, so `N*x+carry=1`, `cnt=6`, `carry=0`

That is `7*15873=111111`.

```java
public int smallestRepunitDivByK(int K) {
    // if `K` ends with 5 or `K` is even, there will never be an answer.
    if (K % 10 == 5 || K % 2 == 0)
        return -1;
    int cnt = 0, carry = 0;
    while (true) {
        for (int i = 0; i < 10; i++) {
            if ((i * K + carry) % 10 == 1) {
                carry = (i * K + carry) / 10;
                cnt++;
                break;
            }
        }
        if (carry == 0)
            break;
    }
    return cnt;
}
```
---

And I find a interesting rule.

Let `3` multiply `0` to `9`, we get `0, 3, 6, 9, 2, 5, 8, 1, 4, 7`.

Let `7` multiply `0` to `9`, we get `0, 7, 4, 1, 8, 5, 2, 9, 6, 3`.

Let `1` multiply `0` to `9`, we get `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`.

Let `9` multiply `0` to `9`, we get `0, 9, 8, 7, 6, 5, 4, 3, 2, 1`.

See what we got?

Every result above covers `0` to `9`. And if we remove `0`, the results of `3` and `7` are just in the reverse order, which holds for `1` and `9`.

---

## Another Smart Solution

It just thinks the problem in another way. Think about how we do division. We keep add `1` at the end of the `cur`, until `cur%K==0`. And we just keep the part of `cur` which  not be divisible by `K`.

```java
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
```


