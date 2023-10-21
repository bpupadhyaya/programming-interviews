// You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i]
// represent the start and the end of the i^{th} interval and intervals is sorted in ascending order by start_i.
// You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
// Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
// still does not have any overlapping intervals (merge overlapping intervals if necessary).
// Return intervals after the insertion.
// Sample 1:
// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]

import java.util.List;
import java.util.ArrayList;
class InsertInterval {
    public  static void main(String...args) {
        int[][] intervals = {{1,3},{6,9}};
        int[] newInterval = {2,5};
        int[][] mergedIntervals = insertInterval(intervals, newInterval);
        for (int i = 0; i < mergedIntervals.length; i++) {
            System.out.print("{");
            for (int j = 0; j < mergedIntervals[i].length; j++) {
                System.out.print(mergedIntervals[i][j] + ", ");
            }
            System.out.print("},");
        }
        System.out.println();

    }

    static int[][] insertInterval(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0, n = intervals.length;
        while (i<n && intervals[i][1] < newInterval[0])
            result.add(intervals[i++]);
        while(i<n && intervals[i][0] <= newInterval[1]) {
            newInterval = new int[]
                    {Math.min(intervals[i][0], newInterval[0]), Math.max(intervals[i][1], newInterval[1])};
            i++;
        }

        result.add(newInterval);
        while (i < n)
            result.add(intervals[i++]);
        return result.toArray(new int[result.size()][2]);
    }
}
