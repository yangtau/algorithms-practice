#include <stdio.h>
int movesToMakeZigzag(int* nums, int numsSize) {
    int evenDecCnt = 0;
    for (int i = 0; i < numsSize; i += 2) {
        int min = 1001;
        if (i + 1 < numsSize && nums[i + 1] < min)
            min = nums[i + 1];
        if (i - 1 >= 0 && nums[i - 1] < min)
            min = nums[i - 1];
        if (nums[i] >= min) {
            evenDecCnt += nums[i] - min + 1;
            // printf("%d\n", nums[i]-min+1);
        }
    }
    int oddDecCnt = 0;
    for (int i = 1; i < numsSize; i += 2) {
        int min = 1001;
        if (i + 1 < numsSize && nums[i + 1] < min)
            min = nums[i + 1];
        if (i - 1 >= 0 && nums[i - 1] < min)
            min = nums[i - 1];
        if (nums[i] >= min) {
            oddDecCnt += nums[i] - min + 1;
        }
    }
    return oddDecCnt > evenDecCnt ? evenDecCnt : oddDecCnt;
}
