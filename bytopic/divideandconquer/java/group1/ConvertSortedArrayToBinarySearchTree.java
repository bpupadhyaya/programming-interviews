// Given an integer array nums where the elements are sorted in ascending order, convert it to a
// height-balanced binary search tree.
// Example:
// Input: nums = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: [0,-10,5,null,-3,null,9] is also accepted.
//
// Tag: 108/150
// Tag: 108/2927, R978/2936 (overall frequency ranking)

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

class SortedArrayToBinarySearchTreeConversion {
    public static void main(String...args) {
        int[] nums = {-10,-3,0,5,9};
        TreeNode root = sortedArrayToBST(nums);
        System.out.print(root.val + "," + root.left.val + "," + root.right.val + ",");
        System.out.print(root.left.right.val + "," + root.right.right.val);
        System.out.println();
    }

    static TreeNode sortedArrayToBST(int[] nums) {
        return createBST(nums, 0, nums.length - 1);
    }

    private static TreeNode createBST(int[] nums, int l, int r) {
        if (l > r) // Base condition or recursion stopping condition
            return null;

        // If we directly create tree in the given sorted order ti will become linked list.
        // So we need to take middle element as head value such that ti will beome height balanced.
        int mid = l + (r-l)/2; // formula to find mid point index
        TreeNode root = new TreeNode(nums[mid]); // mid value or median
        root.left = createBST(nums, l, mid - 1);
        root.right = createBST(nums, mid + 1, r);

        return root;
    }
}