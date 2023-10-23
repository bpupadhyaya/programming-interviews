// Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
// such that adding up all the values along the path equals targetSum.
// A leaf is a node with no children.
// Sample 1:
// Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
// Output: true
// Explanation: The root-to-leaf path with the target sum has leaf node 2.
// Note: visualize to understand

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
class PathSum {
    public static void main(String...args) {
        TreeNode tree = new TreeNode(5);
        TreeNode left = new TreeNode(4);
        tree.left = left;
        TreeNode leftLeft = new TreeNode(11, new TreeNode(7), new TreeNode(2));
        tree.left.left = leftLeft;

        TreeNode right = new TreeNode(8);
        TreeNode rightLeft = new TreeNode(13);
        TreeNode rightRight = new TreeNode(4, null, new TreeNode(1));
        right.left = rightLeft;
        right.right = rightRight;
        tree.right = right;

        int targetSum = 22;
        System.out.println("Path sum exists? " + hasPathSum(tree, targetSum));

    }

    static boolean hasPathSum(TreeNode root, int targetSum) {
        int sum = 0;
        return rootToLeafPathSum(root, targetSum, sum);
    }
    private static boolean rootToLeafPathSum(TreeNode root, int targetSum, int sum) {
        if (root == null)
            return false;
        if (root.left == null && root.right == null) {
            sum = sum + root.val;
            if (sum == targetSum)
                return true;
        }

        return rootToLeafPathSum(root.left, targetSum, sum + root.val)
                || rootToLeafPathSum(root.right, targetSum, sum + root.val);
    }
}
