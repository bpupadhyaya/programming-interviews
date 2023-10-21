// Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
// and return an array of the non-overlapping intervals that cover all the intervals in the input.
// Sample 1:
// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

import java.util.LinkedList;
class MergeInterval {
    public static void main(String...args) {
        int[][] intervals = {{1,3}, {2,6}, {8,10},{15,18}};
        int[][] mergedIntervals = mergeIntervals(intervals);
        for (int i = 0; i < mergedIntervals.length; i++) {
            System.out.print("{");
            for (int j = 0; j < mergedIntervals[i].length; j++) {
                System.out.print(mergedIntervals[i][j] + ", ");
            }
            System.out.print("},");
        }
        System.out.println();
    }
    static int[][] mergeIntervals(int[][] intervals) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < intervals.length; i++) {
            min = Math.min(min, intervals[i][0]);
            max = Math.max(max, intervals[i][0]);
        }

        int[] range = new int[max-min+1];
        for (int i = 0; i < intervals.length; i++) {
            range[intervals[i][0] - min] = Math.max(intervals[i][1] - min, range[intervals[i][0] - min]);
        }

        int start = 0, end = 0;
        LinkedList<int[]> result = new LinkedList<>();
        for (int i = 0; i < range.length; i++) {
            if (range[i] == 0) {
                continue;
            }
            if (i <= end) {
                end = Math.max(range[i], end);
            } else {
                result.add(new int[] {start+min, end+min});
                start = i;
                end = range[i];
            }
        }
        result.add(new int[] {start+min, end+min});

        return result.toArray(new int[result.size()][]);
    }
}