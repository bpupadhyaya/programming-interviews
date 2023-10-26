// Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number
// of conference rooms required.
// Input: intervals = [[0,30],[5,10],[15,20]]
// Output: 2

import java.util.Arrays;
class MeetingRoomsII {
    public static void main(String...args) {
        int[][] intervals = {{0,30},{5,10},{15,20}};
        System.out.println("Min meeting rooms: " + minMeetingRooms(intervals));
    }

    static int minMeetingRooms(int[][] intervals) {
        int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int rooms = 0;
        int endItr = 0;
        for (int i = 0; i < starts.length; i++) {
            if (starts[i] < ends[endItr])
                rooms++;
            else
                endItr++;
        }
        return rooms;
    }
}