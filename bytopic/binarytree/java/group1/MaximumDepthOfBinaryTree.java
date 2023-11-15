// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
// farthest leaf node.
// Example:
// Input: root = [3,9,20,null,null,15,7]
// Output: 3
// Note: Visualize to understand
//
// Tag: 68/150
// Tag: 104/2927, R670/2936 (overall frequency ranking)

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
class MaximumDepthOfBinaryTree {
    public static void main(String...args) {
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println("Max, depth: " + maxDepth(root));
    }

    static int maxDepth(TreeNode root) {
        if (root == null)
            return 0;

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
