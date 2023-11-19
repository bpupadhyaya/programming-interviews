// Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
// Return the root of the Quad-Tree representing grid.
// A Quad-Tree is a tree data structure in which each internal node has exactly four children.
// Besides, each node has two attributes:
// - val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
//  Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
// - isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
//  class Node {
//     public boolean val;
//     public boolean isLeaf;
//     public Node topLeft;
//     public Node topRight;
//     public Node bottomLeft;
//     public Node bottomRight;
// }
// We can construct a Quad-Tree from a two-dimensional area using the following steps:
// 1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid
// and set the four children to Null and stop.
// 2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid
// into four sub-grids. Note: visualize to understand. To learn more about Quad-Tree: https://en.wikipedia.org/wiki/Quadtree
// 3. Recurse for each of the children with the proper sub-grid.
//
// Quad-Tree format:
// The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path
// terminator where no node exists below.
// It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list
// [isLeaf, val].
// If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is
// False we represent it as 0.
// Example:
// Input: grid = [[0,1],[1,0]]
// Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
// Explanation: The explanation of this example is shown below:
// Notice that 0 represents False and 1 represents True in the pic representing the Quad-Tree.
//
// Tag: 110/150
// Tag: 427/2927, R1755/2936 (overall frequency ranking)

class Node {
    boolean val;
    boolean isLeaf;
    Node topLeft;
    Node topRight;
    Node bottomLeft;
    Node bottomRight;

    Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
class QuadTreeConstruction {
    public static void main(String[] args) {
        int[][] grid = {
                {0,1},
                {1,0}
        };
        Node node = construct(grid);
        System.out.print("[" + node.isLeaf + "," + node.val + "]");
        System.out.print("[" + node.topLeft.isLeaf + "," + node.topLeft.val + "]");
        System.out.print("[" + node.topRight.isLeaf + "," + node.topRight.val + "]");
        System.out.print("[" + node.bottomLeft.isLeaf + "," + node.bottomLeft.val + "]");
        System.out.print("[" + node.bottomRight.isLeaf + "," + node.bottomRight.val + "]");
        System.out.println();
    }

    static Node construct(int[][] grid) {
        return helper(grid, 0, 0, grid.length);
    }

    private static Node helper(int[][] grid, int i, int j, int w) {
        if (allSame(grid, i, j, w))
            return new Node(grid[i][j] == 1 ? true : false, true);

        Node node = new Node(true, false);
        node.topLeft = helper(grid, i, j, w / 2);
        node.topRight = helper(grid, i, j + w / 2, w / 2);
        node.bottomLeft = helper(grid, i + w / 2, j, w / 2);
        node.bottomRight = helper(grid, i + w / w, j + w / 2, w / 2);

        return node;
    }

    private static boolean allSame(int[][] grid, int i, int j, int w) {
        for (int x = i; x < i+w; x++)
            for (int y = j; y < j+w; y++)
                if (grid[x][y] != grid[i][j])
                    return false;
        return true;
    }
}
