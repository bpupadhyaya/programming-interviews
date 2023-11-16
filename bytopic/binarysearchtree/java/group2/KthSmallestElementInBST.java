// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
// values of the nodes in the tree.
// Example:
// Input: root = [3,1,4,null,2], k = 1
// Output: 1
//
// Tag: 87/150
// Tag: 230/2927, R731/2936 (overall frequency ranking)

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

class KthSmallestElementInBST {
    private static int value = 0;
    private static int count = 0;
    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(1), new TreeNode(4));
        root.left.right = new TreeNode(2);

        int k = 1;
        System.out.println("Kth smallest: " + kthSmallest(root, k));
    }

    static int kthSmallest(TreeNode root, int k) {
        count = k;
        helper(root);
        return value;
    }

    private static void helper(TreeNode root) {
        if (root.left != null)
            helper(root.left);
        count--;
        if (count == 0) {
            value = root.val;
            return;
        }
        if (root.right != null)
            helper(root.right);
    }
}