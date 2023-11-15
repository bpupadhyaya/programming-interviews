// Given the root of a binary tree, invert the tree, and return its root.
// Example:
// Input: root = [4,2,7,1,3,6,9]
// Output: [4,7,2,9,6,3,1]
// Note: Visualize to understand
//
// Tag: 70/150
// Tag: 226/2927, R757/2936 (overall frequency ranking)

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

class BinaryTreeInversion {
    public static void main(String...args) {
        TreeNode root = new TreeNode(4,
                new TreeNode(2, new TreeNode(1), new TreeNode(3)),
                new TreeNode(7, new TreeNode(6), new TreeNode(9))
        );

        TreeNode inverted = invertTree(root);
        System.out.print(inverted.val + "," + inverted.left.val + "," + inverted.right.val + ",");
        System.out.print(inverted.left.left.val + "," + inverted.left.right.val + ",");
        System.out.print(inverted.right.left.val + "," + inverted.right.right.val);
        System.out.println();
    }

    static TreeNode invertTree(TreeNode root) {
        if (root == null)
            return root;

        invertTree(root.left);
        invertTree(root.right);

        // Swapping
        TreeNode curr = root.left;
        root.left = root.right;
        root.right = curr;
        return root;
    }
}
