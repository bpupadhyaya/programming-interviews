// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
// Sample 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Tag: fb R4/50

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
class TopKFrequentElements {
    public static void main(String...args) {
        int[] nums = {1,1,1,2,2,3};
        int k = 2;
        int[] topKFreq = topKFrequent(nums, k);
        for (int i = 0; i < topKFreq.length; i++)
            System.out.print(topKFreq[i] + ",");
        System.out.println();
    }

    static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i: nums)
            map.merge(i, 1, Integer::sum); // For getting frequency
        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((a, b) -> map.get(b) - map.get(a)); // Sort by frequency in descending order
        int result[] = new int[k];
        for (int i = 0; i < k; i++)
            result[i] = list.get(i);
        return result;
    }
}