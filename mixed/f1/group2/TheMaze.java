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

class TheMaze {
    public static void main(String...args) {
        int maze[][] = {
                {0,0,1,0,0},
                {0,0,0,0,0},
                {0,0,0,1,0},
                {1,1,0,1,1},
                {0,0,0,0,0}
        };
        int start[] = {0,4};
        int destination[] = {4,4};

        System.out.println("Has path? " + hasPath(maze, start, destination));
    }

    static boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int rows = maze.length;
        int cols = maze[0].length;
        boolean[][] visited = new boolean[rows][cols];
        return dfs(maze, start[0], start[1], destination, visited);
    }

    private static boolean dfs(int[][] maze, int row, int col, int[] destination, boolean[][] visited) {
        if (row == destination[0] && col == destination[1]) {
            return true;
        }
        if (visited[row][col]) {
            return false;
        }
        visited[row][col] = true;
        // Try to move all four directions
        return moveThenDFS(maze, row, col, destination, 1, 0, visited) ||
                moveThenDFS(maze, row, col, destination, -1, 0, visited) ||
                moveThenDFS(maze, row, col, destination, 0, 1, visited) ||
                moveThenDFS(maze, row, col, destination, 0, -1 , visited);
    }

    private static boolean moveThenDFS(int[][] maze, int row, int col, int[] destination, int drow, int dcol, boolean[][] visited) {
        int rows = maze.length;
        int cols = maze[0].length;

        int r = row;
        int c = col;
        while (r+drow >= 0 && r+drow <= rows-1 && c+dcol >= 0 && c+dcol <= cols - 1 && maze[r+drow][c+dcol] == 0) {
            r = r + drow;
            c = c + dcol;
        }

        return dfs(maze, r, c, destination, visited);
    }
}