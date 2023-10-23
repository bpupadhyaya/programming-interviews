// You are given the root of a binary tree containing digits from 0 to 9 only.
// Each root-to-leaf path in the tree represents a number.
// For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
// Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will
// fit in a 32-bit integer.
// A leaf node is a node with no children.
// Sample 1:
// Input: root = [4,9,0,5,1]
// Note: visualize to understand : hint: 4 in the first row, 9, 0 in the second row, 5, 1 in the third row.
// Output: 1026
// Explanation:
// The root-to-leaf path 4->9->5 represents the number 495.
// The root-to-leaf path 4->9->1 represents the number 491.
// The root-to-leaf path 4->0 represents the number 40.
// Therefore, sum = 495 + 491 + 40 = 1026.

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
class SumRootToLeafNumbers {
    static int sum = 0;
    public static void main(String...args) {
        TreeNode tree = new TreeNode(4);
        TreeNode right = new TreeNode(0);
        TreeNode left = new TreeNode(9, new TreeNode(5), new TreeNode(1));
        tree.left = left;
        tree.right = right;

        System.out.println("Sum of root to leaf: " + findSumRootToLeaf(tree));
    }

    static int findSumRootToLeaf(TreeNode root) {
        helper(root, "");
        return sum;
    }

    private static void helper(TreeNode root, String str) {
        if (root == null)
            return;

        str += root.val;
        if (root.left == null || root.right == null) {
            sum += Integer.parseInt(str);
            return;
        }

        helper(root.left, str);
        helper(root.right, str);
    }
}
