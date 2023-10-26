// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
// the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
// Sample 1:
// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
// Output: 3
// Explanation: The LCA of nodes 5 and 1 is 3.
// Sample 2:
// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
// Output: 5
// Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
// Note: Visualize to understand. The difference with binary search tree is that binary tree is not sorted, so the
// elements on the left are not necessarily less than elements on the right.
// Note: program has bug, fix to get correct output.

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode (int x) {
        this.val = x;
    }
}
class LowestCommonAncestorOfBinaryTree {
    public static void main(String...args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);
        root.left.right.left = new TreeNode(7);
        root.left.right.right = new TreeNode(4);
        root.right.left = new TreeNode(0);
        root.right.right = new TreeNode(8);

        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);

        TreeNode lowestCommonAnc = lowestCommonAncestor(root,p,q);
        if (lowestCommonAnc != null)
            System.out.println("Lowest common ancestor: " + lowestCommonAnc.val);
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q)
            return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left == null)
            return right;
        else if (right == null)
            return left;
        else
            return root;
    }
}