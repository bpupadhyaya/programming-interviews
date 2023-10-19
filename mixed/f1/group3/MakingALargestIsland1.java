// You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
// Return the size of the largest island in grid after applying this operation.
// An island is a 4-directionally connected group of 1s.
// Sample 1:
// Input: grid = [[1,0],[0,1]]
// Output: 3
// Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

import java.util.Set;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Map;
class MakingALargestIsland1 {
    public static void main(String...args) {
        int[][] mat = {{1,0},{0,1}};
        System.out.println("Size: " + makeLargestIsland(mat));
    }

    static int makeLargestIsland(int[][] grid) {
        Map<Integer, Integer> regionsArea = new HashMap<>();
        regionsArea.put(0,0);

        int n = grid.length;
        int region = 2;

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1){
                    int area = floodFill(grid, i, j, region);
                    regionsArea.put(region, area);
                    region++;
                }
            }
        }

        int max = regionsArea.getOrDefault(2,0);
        for(int r=0; r<n; r++){
            for(int c=0; c<n; c++){
                if(grid[r][c] == 0){
                    Set<Integer> neighbors = new HashSet<>();
                    neighbors.add(r>0? grid[r-1][c] : 0);
                    neighbors.add(c>0? grid[r][c-1] : 0);
                    neighbors.add(r<n-1? grid[r+1][c] : 0);
                    neighbors.add(c<n-1? grid[r][c+1] : 0);
                    int area = 1;
                    for(int neighbor: neighbors){
                        area += regionsArea.get(neighbor);
                    }
                    if(area>max){
                        max = area;
                    }
                }
            }
        }

        return max;
    }

    static int floodFill(int[][] grid, int r, int c, int region) {
        int n = grid.length;
        if(r<0 || r>=n || c<0 || c>=n || grid[r][c]!=1){
            return 0;
        }

        grid[r][c] = region;

        int sum = 1;
        sum+=floodFill(grid, r, c+1, region);
        sum+=floodFill(grid, r+1, c, region);
        sum+=floodFill(grid, r, c-1, region);
        sum+=floodFill(grid, r-1, c, region);

        return sum;
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
