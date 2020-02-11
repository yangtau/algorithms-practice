import java.util.TreeMap;
import java.util.Map.Entry;
import java.util.ArrayList;
import java.util.List;
import java.util.SortedMap;

class TweetCounts {
    TreeMap<String, TreeMap<Integer, Integer>> map;

    public TweetCounts() {
        map = new TreeMap<>();
    }

    public void recordTweet(String tweetName, int time) {
        map.putIfAbsent(tweetName, new TreeMap<>());
        TreeMap<Integer, Integer> rd = map.get(tweetName);
        rd.put(time, rd.getOrDefault(time, 0) + 1);
    }

    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        TreeMap<Integer, Integer> rd = map.get(tweetName);
        for (String en : map.keySet()) {
            System.out.println(en);
        }
        int delta = 60;
        if (freq.equals("hour"))
            delta = 60 * 60;
        else if (freq.equals("day"))
            delta = 60 * 60 * 24;

        int n = (endTime - startTime + delta - 1) / delta;
        List<Integer> res = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            int lo = startTime + i * delta;
            int hi = Math.min(lo + delta, endTime);
            SortedMap<Integer, Integer> subTree = rd.subMap(lo, hi + 1);
            int s = 0;
            for (Entry<Integer, Integer> entry : subTree.entrySet())
                s += entry.getValue();
            res.add(i, s);
        }
        return res;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such: TweetCounts
 * obj = new TweetCounts(); obj.recordTweet(tweetName,time); List<Integer>
 * param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
