// Given a triangle array, return the minimum path sum from top to bottom.
// For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the
// current row, you may move to either index i or index i + 1 on the next row.
// Example:
// Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
// Output: 11
// Explanation: The triangle looks like:
//    2
//   3 4
//  6 5 7
// 4 1 8 3
// The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
//
// Tag: 142/150
// Tag: 120/2927, R497/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Triangle {
    private static Integer[][] memo;
    public static void main(String...args) {
        Integer[][] triangle = {{2},{3,4},{6,5,7},{4,1,8,3}};
        List<List<Integer>> triangleList = new ArrayList<>();
        for (Integer[] rowArray: triangle) {
            triangleList.add(Arrays.asList(rowArray));
        }
        System.out.println("Minimum total: " + minimumTotal(triangleList));
    }

    static int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        memo = new Integer[n][n];
        return dfs(0, 0, triangle);
    }

    static int dfs(int level, int i, List<List<Integer>> triangle) {
        if (memo[level][i] != null) return memo[level][i];

        int path = triangle.get(level).get(i);
        if (level < triangle.size() - 1)
            path += Math.min(dfs(level +1, i, triangle), dfs(level+1, i+1, triangle));

        return memo[level][i] = path;
    }
}

// Time complexity ~ O(n^2)
// Space complexity ~ O(n^2)