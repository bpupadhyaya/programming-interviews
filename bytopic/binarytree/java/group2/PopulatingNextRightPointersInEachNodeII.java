// Given a binary tree
//
// struct Node {
//   int val;
//   Node *left;
//   Node *right;
//   Node *next;
// }
// Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
// should be set to NULL.
// Initially, all next pointers are set to NULL.
// Example:
// Input: root = [1,2,3,4,5,null,7]
// Output: [1,#,2,3,#,4,5,7,#]
// Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to
// its next right node, just like in Figure B. The serialized output is in level order as connected by the
// next pointers, with '#' signifying the end of each level.
// Note: Visualize to understand (the element horizontally right is the next pointer in visualization, # is null)
//
// Tag: 74/150
// Tag: 117/2927, R1731/2936 (overall frequency ranking)
// Note: Program compiles but has runtime error. Debug and fix.

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode next;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right, TreeNode next) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.next = next;
    }
}

class PopulatingNextRightPointersInEachNodeII {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5), null),
            new TreeNode(3, null, new TreeNode(7), null), null
        );

        TreeNode result = connect(root);
        System.out.print(result.val + "," + result.next.val + "," + result.left.val + "," + result.left.next.val + "," +
                result.right.next.val + "," + result.left.left.val + "," + result.left.left.next.val + "," +
                result.left.right.next.val + "," + result.right.right.next.val);
    }

    static TreeNode connect(TreeNode root) {
        TreeNode dummyHead = new TreeNode(0); // this head will always point to the first element in the current layer we are searching
        TreeNode pre = dummyHead; // this 'pre' will be the "current node" that builds every single layer
        TreeNode realRoot = root; // For return

        while (root != null) {
            if (root.left != null) {
                pre.next = root.left;
                pre = pre.next;
            }

            if (root.right != null) {
                pre.next = root.right;
                pre = pre.next;
            }
            root = root.next;
            if (root == null) { // Reach the end of current layer
                pre = dummyHead; // Shift pre back to the beginning, get ready to point to the first element in next layer
                root = dummyHead.next; // root comes down one level below to the first available non null node
                dummyHead.next = null; // Reset dummyhead back to default null
            }
        }
        return realRoot;
    }
}
