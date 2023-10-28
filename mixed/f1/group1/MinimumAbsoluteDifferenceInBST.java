// Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any
// two different nodes in the tree.
// Sample 1:
// Input: root = [4,2,6,1,3]
// Output: 1

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {};
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class MinimumAbsoluteDifferenceInBST {
    static int prev = Integer.MAX_VALUE;
    static int ans = Integer.MAX_VALUE;
    public static void main(String...args) {
        TreeNode root = new TreeNode(4, new TreeNode(2), new TreeNode(6));
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        System.out.println("Min. diff.: " + getMinimumDifference(root));
    }

    static int getMinimumDifference(TreeNode root) {
        inOrder(root);
        return ans;
    }
    static void inOrder(TreeNode root) {
        if (root.left != null)
            inOrder(root.left);
        ans = Math.min(ans, Math.abs(root.val - prev));
        prev = root.val;
        if (root.right != null)
            inOrder(root.right);
    }
}
