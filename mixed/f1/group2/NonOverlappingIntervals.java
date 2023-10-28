// Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals
// you need to remove to make the rest of the intervals non-overlapping.
// Sample 1:
// Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

import java.util.Arrays;
class NonOverlappingIntervals {
    public static void main(String...args) {
        int[][] intervals = {{1,2},{2,3},{3,4},{1,3}};
        System.out.println("How many removed? " + eraseOverlapIntervals(intervals));
    }

    static int eraseOverlapIntervals(int[][] intervals) {
        int n = intervals.length;
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[1], b[1]));

        int prev = 0;
        int count = 1;

        for (int i = 1; i < n; i++) {
            if (intervals[i][0] >= intervals[prev][1]) {
                prev = i;
                count++;
            }
        }
        return n - count;
    }
}