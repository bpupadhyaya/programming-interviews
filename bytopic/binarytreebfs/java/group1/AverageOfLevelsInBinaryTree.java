// Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
// Answers within 10^{-5} of the actual answer will be accepted.
// Example:
// Input: root = [3,9,20,null,null,15,7]
// Output: [3.00000,14.50000,11.00000]
// Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
// Hence return [3, 14.5, 11].
// Note: Visualize the binary tree to understand
//
// Tag: 82/150
// Tag: 199/2927, R549/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;
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

class AverageOfLevelsInBinaryTree {
    public static void main(String...args) {
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<Double> result = averageOfLevels(root);
        for (Double avg: result)
            System.out.print(avg + ",");
        System.out.println();
    }

    static List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null)
            return result;

        queue.add(root);
        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            double sum = 0.0;
            for (int i = 0; i < queueSize; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }
            result.add(sum/queueSize);
        }
        return result;
    }
}
