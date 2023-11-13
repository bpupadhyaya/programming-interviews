// There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are
// represented as a 2D integer array points where points[i] = [x_start, x_end] denotes a balloon whose horizontal
// diameter stretches between x_start and x_end. You do not know the exact y-coordinates of the balloons.
// Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
// A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. There is no limit to the
// number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
// Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
// Example:
// Input: points = [[10,16],[2,8],[1,6],[7,12]]
// Output: 2
// Explanation: The balloons can be burst by 2 arrows:
// - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
// - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
// 51/150

import java.util.Arrays;
class MinimumNumberOfArrowsToBurstBaloons {
    public static void main(String...args) {
        int[][] points = {{10,16},{2,8},{1,6},{7,12}};
        System.out.println("Min number of arrows: " + findMinArrowShots(points));
    }

    static int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }

        Arrays.sort(points, (a,b) -> a[1] - b[1]);
        int arrowPosition = points[0][1];
        int arrrowCount = 1;
        for (int i = 1; i < points.length; i++) {
            if (arrowPosition >= points[i][0]) {
                continue;
            }
            arrrowCount++;
            arrowPosition = points[i][1];
        }
        return arrrowCount;
    }
}