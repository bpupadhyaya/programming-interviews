// You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent
// the start and the end of the i^{th} interval and intervals is sorted in ascending order by start_i. You are also
// given an interval newInterval = [start, end] that represents the start and end of another interval.
// Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals
// still does not have any overlapping intervals (merge overlapping intervals if necessary).
// Return intervals after the insertion.
// Example:
// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
// Tag: 50/150

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class IntervalInsertion {
    public static void main(String...args) {
        int[][] intervals = {{1,2}, {3,5},{6,7},{8,10},{12,16}};
        int[] newInterval = {4,8};
        int[][] result = insert(intervals, newInterval);
        for (int[] range: result)
            System.out.print(Arrays.toString(range) + ",");
        System.out.println();
    }

    static int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        // Iterate through all slots
        for (int[] slot: intervals) {
            // if newInterval is before the first slot, insert it and update slot as newInterval.
            if (newInterval[1] < slot[0]) {
                result.add(newInterval);
                newInterval = slot;
            }

            // If slot is less than newInterval, insert slot
            else if (slot[1] < newInterval[0]) {
                result.add(slot);
            }

            // If above conditions fail, it is an overlap.
            // Update lowest of start and highest of end and do not insert.
            else {
                newInterval[0] = Math.min(newInterval[0], slot[0]);
                newInterval[1] = Math.max(newInterval[1], slot[1]);
            }
        }

        // Insert the last newInterval.
        result.add(newInterval);

        // Convert to int[][] array and return.
        return result.toArray(new int[result.size()][]);
    }
}