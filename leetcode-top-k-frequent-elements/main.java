import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.stream.Collectors;
import java.util.function.Function;

class Solution {
    public List<Integer> topKFrequent_stream(int[] nums, int k) {
        return Arrays.stream(nums).boxed().collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())).limit(k)
                .map(Map.Entry::getKey).collect(Collectors.toList());
    }

    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int i : nums)
            frequencyMap.put(i, frequencyMap.getOrDefault(i, 0) + 1);
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        pq.addAll(frequencyMap.entrySet());
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < k; i++)
            res.add(pq.poll().getKey());
        return res;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 1, 1, 2, 3, 4, 3, 3, 4, 5 };
        int k = 3;
        var res = new Solution().topKFrequent(nums, k);
        System.out.println(res.toString());
    }
}