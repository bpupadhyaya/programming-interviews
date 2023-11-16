// Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
// inorder is the inorder traversal of the same tree, construct and return the binary tree.
// Example:
// Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
// Output: [3,9,20,null,null,15,7]
//
// Tag: 72/150
// Tag: 101/2927, R485/2936 (overall frequency ranking)


import java.util.Arrays;
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

class BinaryTreeConstructionFromPreorderAndInorderTraversal {
    public static void main(String...args) {
        int[] preorder = {3,9,20,15,7};
        int[] inorder = {9,3,15,20,7};

        TreeNode root = buildTree(preorder, inorder);
        System.out.print(root.val + "," + root.left.val + "," + root.right.val + ",");
        System.out.print(root.right.left.val + "," + root.right.right.val);
        System.out.println();
    }

    static TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0)
            return null;

        TreeNode root = new TreeNode(preorder[0]);
        if (preorder.length == 1)
            return root;

        int breakIndex = -1;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == preorder[0]) {
                breakIndex = i;
                break;
            }
        }

        int[] subLeftPre = Arrays.copyOfRange(preorder, 1, breakIndex + 1);
        int[] subLeftIn = Arrays.copyOfRange(inorder, 0, breakIndex);
        int[] subRightPre = Arrays.copyOfRange(preorder, breakIndex + 1, preorder.length);
        int[] subRightIn = Arrays.copyOfRange(inorder, breakIndex + 1, inorder.length);

        root.left = buildTree(subLeftPre, subLeftIn);
        root.right = buildTree(subRightPre, subRightIn);

        return root;
    }
}