/* https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/ */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MOD ((int)(1e9) + 7)

/*
 * num_roll_to_target:
 * d dice, each die has f face,
 * return the number of ways to roll the dice to the target.
 */
int num_rolls_to_target(int d, int f, int target) {
    int memo[target + 1][d + 1];

    for (int i = 0; i <= target; i++) {
        for (int j = 0; j <= d; j++) {
            memo[i][j] = 0;
        }
    }

    for (int i = 1; i <= f; i++) {
        memo[i][1] = 1;
    }

    for (int n = 1; n <= target; n++) {
        for (int part = 2; part <= d; part++) {
            for (int i = 1; i <= f && n - i >= part - 1; i++) {
                memo[n][part] += memo[n - i][part - 1];
                memo[n][part] %= MOD;
            }
        }
    }

    return memo[target][d];
}

/*
 * numRollsToTarget:
 * an implementation with better space performance.
 */
int numRollsToTarget(int d, int f, int target) {
    // int memo[target + 1][d + 1];
    int a[target + 1];
    int b[target + 1];

    for (int i = 1; i <= target; i++) {
        a[i] = i <= f ? 1 : 0;
    }

    int *last = a;
    int *cur = b;

    for (int part = 2; part <= d; part++) {
        for (int n = 1; n <= target; n++) {
            int sum = 0;
            for (int i = 1; i <= f && n - i >= part - 1; i++) {
                sum += last[n - i];
                sum %= MOD;
            }
            cur[n] = sum;
        }
        int *t = last;
        last = cur;
        cur = t;
    }

    return last[target];
}

int main(int argc, char *argv[]) {
    printf("%d\n",
           num_rolls_to_target(atoi(argv[1]), atoi(argv[2]), atoi(argv[3])));
    return 0;
}
