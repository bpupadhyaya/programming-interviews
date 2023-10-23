// Given the root of a binary tree, return the zigzag level order traversal of its nodes'
// values. (i.e., from left to right, then right to left for the next level and alternate between).
// Sample 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[20,9],[15,7]]
// Note: visualize to understand
// It is row level traversal starting from first row, which is root node. First left to right, then right to
// left and again left to right and so on.


import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class BinaryTreeLevelOrderTraversal {
    public static void main(String...args) {
        TreeNode tree = new TreeNode(3);
        TreeNode left = new TreeNode(9);
        TreeNode right = new TreeNode(20, new TreeNode(15), new TreeNode(7));
        tree.left = left;
        tree.right = right;

        List<List<Integer>> zOrder = zigzagLevelOrder(tree);
        for (List<Integer> elem: zOrder) {
            System.out.print(elem + ", ");
        }
        System.out.println();
    }

    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> sol = new ArrayList<>();
        traverse(root, sol, 0);

        return sol;
    }

    static void traverse(TreeNode curr, List<List<Integer>> sol, int level) {
        if (curr == null)
            return;

        if (sol.size() <= level) {
            List<Integer> newLevel = new LinkedList<>();
            sol.add(newLevel);
        }

        List<Integer> collection = sol.get(level);
        if (level % 2 == 0)
            collection.add(curr.val);
        else collection.add(0, curr.val);

        traverse(curr.left, sol, level + 1);
        traverse(curr.right, sol, level + 1);
    }
}