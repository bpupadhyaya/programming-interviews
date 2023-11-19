// Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number
// of points that lie on the same straight line.
// Example:
// Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
// Output: 4
// Note: Visualization may be needed to understand
//
// Tag: 136/150
// Tag: 149/2927, R151/2936 (overall frequency ranking)
// Note: Program compiles but output is not correct, debug and find out.


import java.util.HashMap;
import java.util.Map;
class MaxPointsOnALine {
    public static void main(String[] args) {
        int[][] points = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
        System.out.println("Max. points on a line: " + maxPoints(points));
    }

    static int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 2) return n;
        int ans = 2;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = 2;
                for (int k = j + 1; k < n; k++) {
                    int x = (points[j][1] - points[i][1] * (points[k][0] - points[i][0]));
                    int y = (points[k][1] - points[i][1]) * (points[j][0] - points[i][0]);
                    if (x == y) {
                        temp++;
                    }
                }
                if (temp > ans) {
                    ans = temp;
                }
            }
        }

        return ans;
    }
}
