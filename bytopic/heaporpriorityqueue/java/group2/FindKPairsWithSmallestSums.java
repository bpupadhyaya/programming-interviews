// You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
// Define a pair (u, v) which consists of one element from the first array and one element from the second array.
// Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
// Example 1:
// Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
// Output: [[1,2],[1,4],[1,6]]
// Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
// Example 2:
// Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
// Output: [[1,1],[1,1]]
// Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
// Example 3:
// Input: nums1 = [1,2], nums2 = [3], k = 3
// Output: [[1,3],[2,3]]
// Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
//
// Tag: 123/150
// Tag: 373/2927, R380/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
class FindingKPairsWithSmallestSums {
    public static void main(String...args) {
        int[] nums1 = {1,7,11};
        int[] nums2 = {2,4,6};
        int k = 3;
        List<List<Integer>> kPairs = kSmallestPairs(nums1, nums2, k);
        for (List<Integer> pair: kPairs)
            System.out.print(pair + ",");
        System.out.println();
    }

    static List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        // Priority queue to store pairs with smallest sums, sorted by the sum
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        for (int x: nums1) {
            // The sum and the index of the second element in nums2
            pq.offer(new int[]{x + nums2[0], 0});
        }

        // Pop the k smallest pairs from the priority queue
        while (k > 0 && !pq.isEmpty()) {
            int[] pair = pq.poll();
            int sum = pair[0]; // Get the smallest
            int pos = pair[1]; // Get the index of the second element in num2

            List<Integer> currentPair = new ArrayList<>();
            currentPair.add(sum - nums2[pos]);
            currentPair.add(nums2[pos]);
            result.add(currentPair); // Add the pair to the result list

            // If there are more elements in nums2, push the next pair into the priority queue
            if (pos + 1 < nums2.length) {
                pq.offer(new int[] {sum - nums2[pos] + nums2[pos + 1], pos + 1});
            }
            k--;
        }

        return result;
    }
}