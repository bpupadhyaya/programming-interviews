// Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
// Sample 1:
// Input: root = [1,3,2,5,3,null,9]
// Output: [1,3,9]
// Note: visualize to understand
// Soln: BFS

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class FindLargestValueInEachTreeRow {
    public static void main(String...args) {
        TreeNode root = new TreeNode(1, new TreeNode(3), new TreeNode(2));
        root.left.left = new TreeNode(5);
        root.left.right = new TreeNode(3);
        root.right.right = new TreeNode(9);

        List<Integer> largestValues = largestValues(root);
        System.out.println("Largest values: " + largestValues);
    }

    static List<Integer> largestValues(TreeNode root) {
        if (root == null)
            return new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int currLevelSize = queue.size();
            int maxValue = Integer.MIN_VALUE;

            for (int i = 0; i < currLevelSize; i++) {
                TreeNode node = queue.poll();
                maxValue = Math.max(maxValue, node.val);

                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }
            result.add(maxValue);
        }

        return result;
    }
}