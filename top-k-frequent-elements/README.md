## [Problem](https://leetcode.com/problems/top-k-frequent-elements/)
Given a non-empty array of integers, return the k most frequent elements.
**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```
## Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Solution using Java Stream

`O(N*logN)`

### steps:

- count the frequency of numbers in `nums` with a `Map<Integer, Integer>`.
- sort the `map` by value in descending order, thereby sort it by the frequency of the key.
- take the first `k` keys in the map.

Functional programming is so cool :).
```java
public List<Integer> topKFrequent(int[] nums, int k) {
        return Arrays.stream(nums)
                .boxed()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .limit(k)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }
```

## Solution using Priority Queue

`O(N*logN)`

### steps:

- count the frequency of numbers in `nums` with a `Map<Integer, Integer>`.
- put the MapEntry into a Priority-Queue 
- take the first `k` keys in the queue.

---
If the biggest number is not so big, bucket sort is a good choice.
