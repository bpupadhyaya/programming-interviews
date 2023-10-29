// Given the root of a binary tree, return the length of the diameter of the tree.
// The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or
// may not pass through the root.
// The length of a path between two nodes is represented by the number of edges between them.
// Sample 1:
// Input: root = [1,2,3,4,5]
// Output: 3
// Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
// Note: Visualize to understand

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){}
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class DiameterOfBinaryTree {
    static int ans = 0;
    public static void main(String...args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println("Diameter of binary tree: " + diameterOfBinaryTree(root));
    }

    static int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;
        height(root);

        return ans;
    }

    static int height(TreeNode root) {
        if (root == null)
            return -1;
        int l = height(root.left);
        int r = height(root.right);
        ans = Math.max(ans, l+r+2);

        return 1 + Math.max(l,r);
    }
}