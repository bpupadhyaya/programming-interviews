// Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
// For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1)
// and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
// The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index
// starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same
// row and same column. In such a case, sort these nodes by their values.
// Return the vertical order traversal of the binary tree.
// Input: root = [3,9,20,null,null,15,7]
// Output: [[9],[3,15],[20],[7]]
// Explanation:
// Column -1: Only node 9 is in this column.
// Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
// Column 1: Only node 20 is in this column.
// Column 2: Only node 7 is in this column.
// Note: program revisit required, output is correct but not in right format.
// Tag: fb R7/50

import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Comparator;

class Tree {
    int value;
    Tree left;
    Tree right;
    Tree(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
    Tree(int value, Tree left, Tree right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
    public int getValue() {
        return this.value;
    }
    public void setValue(int value) {
        this.value = value;
    }
    public Tree getLeft() {
        return this.left;
    }
    public void setLeft(Tree left) {
        this.left = left;
    }
    public Tree getRight() {
        return this.right;
    }
    public void setRight(Tree right) {
        this.right = right;
    }

}

class Point {
    int x, y, val;
    Point(int x, int y, int val) {
        this.x = x;
        this.y = y;
        this.val = val;
    }
}
class BinaryTreeVerticalOrderTraversal {
    public static void main(String...args) {
        Tree tree = new Tree(3);
        tree.setLeft(new Tree(9));
        Tree rightSubTree = new Tree(20);
        rightSubTree.setLeft(new Tree(15));
        rightSubTree.setRight(new Tree(7));
        tree.setRight(rightSubTree);

        List<List<Integer>> result = verticalTraversal(tree);
        for (List<Integer> list: result)
            System.out.println(list);
        System.out.println();
    }

    static List<List<Integer>> verticalTraversal(Tree tree) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        PriorityQueue<Point> pq = new PriorityQueue<Point>(1005, new Comparator<Point>(){
           public int compare(Point p1, Point p2) {
               if (p1.x < p2.x) return -1;
               if (p2.x < p1.x) return 1;
               if (p1.y > p2.y) return -1;
               if (p1.y < p2.y) return 1;

               return p1.val - p2.val;
           }
        });

        verticalTraversalHelper(tree, 0, 0, pq);
        Point prev = null;
        List<Integer> l = new ArrayList<>();
        while(!pq.isEmpty()) {
            Point p = pq.poll();
            if (prev == null || p.x != prev.x) {
                if (prev != null)
                    res.add(l);
            }
            l.add(p.val);
            prev = p;
        }
        res.add(l);
        return res;
    }

    static void verticalTraversalHelper(Tree tree, int x, int y, PriorityQueue<Point> pq)  {
        if (tree == null) return;
        pq.offer(new Point(x, y, tree.value));
        verticalTraversalHelper(tree.left, x-1, y-1, pq);
        verticalTraversalHelper(tree.right, x+1, y-1, pq);
    }

}