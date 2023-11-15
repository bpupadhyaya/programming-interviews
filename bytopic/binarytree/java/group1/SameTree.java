// Given the roots of two binary trees p and q, write a function to check if they are the same or not.
// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
// Example 1:
// Input: p = [1,2,3], q = [1,2,3]
// Output: true
// Example 2:
// Input: p = [1,2], q = [1,null,2]
// Output: false
// Example 3:
// Input: p = [1,2,1], q = [1,1,2]
// Output: false
//
// Tag: 69/150
// Tag: 100/2927, R1007/2936 (overall frequency ranking)

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

class SameTree {
    public static void main(String[] args) {
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode q = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode r = new TreeNode(1, new TreeNode(2), null);
        TreeNode s = new TreeNode(1, null, new TreeNode(2));
        System.out.println("Same tree? " + isSameTree(r, s));
    }

    static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;

        if (p == null || q == null || p.val != q.val)
            return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}