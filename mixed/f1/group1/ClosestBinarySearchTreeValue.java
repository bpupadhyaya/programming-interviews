// Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
// If there are multiple answers, print the smallest.
// Sample 1:
// Input: root = [4,2,5,1,3], target = 3.714286
// Output: 4
// Note: Visualize to understand.
// Tag: fb R46/50

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

class ClosestBinarySearchTreeValue {
    public static void main(String...args) {
        double target = 3.714286;
        TreeNode root = new TreeNode(4, new TreeNode(2), new TreeNode(5));
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        System.out.println("Closest binary search tree value: " + closestValue(root, target));
    }

    static int closestValue(TreeNode root, double target) {
        int closestValue = root.val;

        while (root != null) {
            int curr = root.val;
            closestValue = Math.abs(curr - target) < Math.abs(closestValue - target) ? curr : closestValue;
            root = target < root.val ? root.left : root.right;
        }
        return closestValue;
    }
}