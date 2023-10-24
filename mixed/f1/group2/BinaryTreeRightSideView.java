// Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
// you can see ordered from top to bottom.
// Sample 1:
// Input: root = [1,2,3,null,5,null,4]
// Output: [1,3,4]
// Note: visualize to understand

import java.util.ArrayList;
import java.util.List;
 class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class BinaryTreeRightSideView {
    static int maxLevel = 0;
    public static void main(String...args) {
        TreeNode root = new TreeNode(1);

        TreeNode left = new TreeNode(2, null, new TreeNode(5));
        root.left = left;
        TreeNode right = new TreeNode(3, null, new TreeNode(4));
        root.right = right;

        List<Integer> rightSide = rightSideView(root);
        for (Integer elem: rightSide)
            System.out.print(elem + ",");
        System.out.println();

    }

    static List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        right(root, 1, list);

        return list;
    }

    static void right(TreeNode root, int level, List<Integer> list) {
        if (root == null)
            return;
        if (maxLevel < level) {
            list.add(root.val);
            maxLevel = level;
        }
        right(root.right, level+1, list);
        right(root.left, level+1, list);
    }
}