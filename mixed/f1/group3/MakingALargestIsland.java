// You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
// Return the size of the largest island in grid after applying this operation.
// An island is a 4-directionally connected group of 1s.
// Sample 1:
// Input: grid = [[1,0],[0,1]]
// Output: 3
// Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
// Note: find alternative to javafx.util.Pair in order to compile

import java.util.ArrayList;
import javafx.util.Pair;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;

class MakingALargestIsland {
    public static int N = 0;
    public static void main(String...args) {
        int[][] mat = {{1,0},{0,1}};
        System.out.println("Size: " + makeLargestIsland(mat));
    }

    static int makeLargestIsland(int[][] mat) {
        N = mat.length;
        // DFS every island and give it an index of island
        int index = 3, res = 0;
        HashMap<Integer, Integer> area = new HashMap<>();
        for (int x = 0; x < N; x++)
            for (int y = 0; y < N; y++)
                if (mat[x][y] == 1) {
                    area.put(index, dfs(mat, x, y, index));
                    res = Math.max(res, area.get(index++));
                }

        // Traverse every 0 cell and count largest island it can connect
        for (int x = 0; x < N; x++)
            for (int y = 0; y < N; y++)
                if (mat[x][y] == 0) {
                    HashSet<Integer> seen = new HashSet<>();
                    int cur = 1;
                    for (Pair<Integer, Integer> p: move(x,y)) {
                        index = mat[p.getKey()][p.getValue()];
                        if (index > 1 && !seen.contains(index)) {
                            seen.add(index);
                            cur += area.get(index);
                        }
                    }
                    res = Math.max(res, cur);
                }
        return res;
    }

    static List<Pair<Integer, Integer>> move(int x, int y) {
        ArrayList <Pair<Integer, Integer>> res = new ArrayList<>();
        if (valid(x, y+1))
            res.add(new Pair<Integer, Integer>(x, y+1));
        if (valid(x, y-1))
            res.add(new Pair<Integer, Integer>(x, y-1));
        if (valid(x+1, y))
            res.add(new Pair<Integer, Integer>(x+1, y));
        if (valid(x-1, y))
            res.add(new Pair<Integer, Integer>(x-1, y));

        return res;
    }

    static boolean valid(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    static int dfs(int[][] grid, int x, int y, int index) {
        int area = 0;
        grid[x][y] = index;
        for(Pair<Integer, Integer> p: move(x, y))
            if (grid[p.getKey()][p.getValue()] == 1)
                area += dfs(grid, p.getKey(), p.getValue(), index);

        return area + 1;
    }

}

// Several simple sub function to help on this kind of problem.
// valid(int x, int y), check if (x, y) is valid in the grid.
// move(int x, int y), return all possible next position in 4 directions.
// Explanation:
// Steps:
// 1. Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
// 2. Loop every cell == 0, check its connected islands and calculate total islands area.
// Complexity:
// Time O(N^2)
// Space O(N^2)
