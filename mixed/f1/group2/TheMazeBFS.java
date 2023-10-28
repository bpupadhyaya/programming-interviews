// There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through
// the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops,
// it could choose the next direction.
// Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and
// destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
// You may assume that the borders of the maze are all walls (see examples).
// Sample 1:
// Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
// Output: true
// Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
// Soln: BFS
// let n = rows, m = cols
// TC: ~O(nm) since we visit each cell once at most
// SC: ~O(nm) since the visited array and call stack

import java.util.Deque;
import java.util.ArrayDeque;
class Cell {
    public int row;
    public int col;
    public Cell (int row, int col) {
        this.row = row;
        this.col = col;
    }
}
class TheMazeBFS {
    private static int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    public static void main(String... args) {
        int maze[][] = {
                {0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0},
                {1, 1, 0, 1, 1},
                {0, 0, 0, 0, 0}
        };
        int start[] = {0, 4};
        int destination[] = {4, 4};

        System.out.println("Has path? " + hasPath(maze, start, destination));
    }

    static boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int rows = maze.length;
        int cols = maze[0].length;
        boolean[][] visited = new boolean[rows][cols];

        Deque<Cell> q = new ArrayDeque<>();
        q.addFirst(new Cell(start[0], start[1]));
        visited[start[0]][start[1]] = true;

        while (q.size() > 0) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                Cell cell = q.removeLast();

                int r = cell.row;
                int c = cell.col;

                if (r == destination[0] && c == destination[1]) {
                    return true;
                }

                for (int[] dir: dirs) {
                    int nextRow = r;
                    int nextCol = c;
                    while (nextRow + dir[0] >= 0 && nextRow + dir[0] < rows && nextCol + dir[1] >= 0 && nextCol + dir[1] < cols && maze[nextRow + dir[0]][nextCol + dir[1]] == 0) {
                        nextRow = nextRow + dir[0];
                        nextCol = nextCol + dir[1];
                    }

                    if (!visited[nextRow][nextCol]) {
                        q.addFirst(new Cell(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }

        return false;
    }
}