// A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
// connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass
// through the root.
// The path sum of a path is the sum of the node's values in the path.
// Given the root of a binary tree, return the maximum path sum of any non-empty path.
// Example:
// Input: root = [-10,9,20,null,null,15,7]
// Output: 42
// Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
// Note: Visualize to understand
//
// Tag: 78/150
// Tag: 124/2927, R96/2936 (overall frequency ranking)


import java.util.Deque;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.Map;

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

class BinaryTreeMaximumPathSum {
    public static void main(String...args) {
        TreeNode root = new TreeNode(-10, new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println("Max path sum: " + maxPathSum(root));
    }

    static int maxPathSum(TreeNode root) {
        int result = Integer.MIN_VALUE;
        Map<TreeNode, Integer> maxRootPath = new HashMap<>(); // Cache
        maxRootPath.put(null, 0); // For simplicity, we want to handle null node
        for (TreeNode node: topSort(root)) {
            // As we process nodes in post-order their children are already cached
            int left = Math.max(maxRootPath.get(node.left), 0);
            int right = Math.max(maxRootPath.get(node.right), 0);
            maxRootPath.put(node, Math.max(left, right) + node.val);
            result = Math.max(left + right + node.val, result);
        }
        return result;
    }

    // Returns the nodes in post-order
    private static Iterable<TreeNode> topSort(TreeNode root) {
        Deque<TreeNode> result = new LinkedList<>();
        if (root != null) {
            Deque<TreeNode> stack = new LinkedList<>();
            stack.push(root);
            while (!stack.isEmpty()) {
                TreeNode curr = stack.pop();
                result.push(curr);
                if (curr.right != null)
                    stack.push(curr.right);
                if (curr.left != null)
                    stack.push(curr.left);
            }
        }
        return result;
    }
}