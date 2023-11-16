// Given the root of a complete binary tree, return the number of the nodes in the tree.
// According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
// and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the
// last level h.
// Design an algorithm that runs in less than O(n) time complexity.
// Example:
// Input: root = [1,2,3,4,5,6]
// Output: 6
//
// Tag: 80/150
// Tag: 222/2927, R1538/2936 (overall frequency ranking)


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

class CountingCompleteTreeNode {
    public static void main(String...args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);

        System.out.println("Nodes count: " + countNodes(root));
    }

    static int countNodes(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}