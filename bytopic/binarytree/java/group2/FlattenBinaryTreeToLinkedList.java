// Given the root of a binary tree, flatten the tree into a "linked list":
// The "linked list" should use the same TreeNode class where the right child pointer points to the next
// node in the list and the left child pointer is always null.
// The "linked list" should be in the same order as a pre-order traversal of the binary tree.
// Sample 1:
// Input: root = [1,2,5,3,4,null,6]
// Output: [1,null,2,null,3,null,4,null,5,null,6]
// Note: Visualize to understand, note that the binary tree is sorted by nature.
//
// Tag: 75/150
// Tag: 114/2927, R646/2936 (overall frequency ranking)

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
class FlattenBinaryTreeToLinkedList {
    public static void main(String...args) {
        TreeNode tree = new TreeNode(1);
        TreeNode left = new TreeNode(2, new TreeNode(3), new TreeNode(4));
        tree.left = left;

        TreeNode right = new TreeNode(5);
        TreeNode rightRight = new TreeNode(6);
        right.right = rightRight;
        tree.right = right;

        flattenTree(tree);

        TreeNode curr = tree;
        while (curr != null) {
            System.out.print(curr.val + ",");
            curr = curr.right;
        }
        System.out.println();
    }

    static void flattenTree(TreeNode root) {
        if (root == null)
            return;

        TreeNode left = root.left;
        TreeNode right = root.right;

        flattenTree(left);
        flattenTree(right);

        root.right = left;
        TreeNode curr = root;
        while (curr.right != null)
            curr = curr.right;
        curr.right = right;
    }
}