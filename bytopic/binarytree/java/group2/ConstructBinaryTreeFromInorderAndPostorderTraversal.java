// Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder
// is the postorder traversal of the same tree, construct and return the binary tree.
// Example:
// Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
// Output: [3,9,20,null,null,15,7]
//
// Tag: 73/150
// Tag: 106/2927, R1542/2936 (overall frequency ranking)

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

class BinaryTreeConstructionFromInorderAndPostorderTraversal {
    public static void main(String...args) {
        int[] inorder = {9,3,15,20,7};
        int[] postorder = {9,15,7,20,3};

        TreeNode root = buildTree(inorder, postorder);
        System.out.print(root.val + "," + root.left.val + "," + root.right.val + ",");
        System.out.print(root.right.left.val + "," + root.right.right.val);
        System.out.println();
    }

    static TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTreeHelper(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
    }

    private static TreeNode buildTreeHelper(int[] inorder, int inStart, int inEnd,
                                            int[] postorder, int postStart, int postEnd) {
        // Base case
        if (inStart > inEnd || postStart > postEnd)
            return null;

        // Find the root node from the last element of postorder traversal
        int rootVal = postorder[postEnd];
        TreeNode root = new TreeNode(rootVal);

        // Find the index of the root node in inorder traversal
        int rootIndex = 0;
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        // Recursively build the left and right subtrees
        int leftSize = rootIndex - inStart;
        int rightSize = inEnd - rootIndex;
        root.left = buildTreeHelper(inorder, inStart, rootIndex - 1, postorder, postStart, postStart + leftSize - 1);
        root.right = buildTreeHelper(inorder, rootIndex + 1, inEnd, postorder, postEnd - rightSize, postEnd - 1);

        return root;
    }
}

// Analysis:
// Inorder traversal visits the nodes in ascending order of their values, i.e., left child, parent, and right child.
// On the other hand, postorder traversal visits the nodes in the order left child, right child, and parent.
// Knowing this, we can say that the last element in the postorder array is the root node, and its index in the inorder
// array divides the tree into left and right subtrees. We can recursively apply this logic to construct the entire
// binary tree.

// Steps:
// 1. Start with the last element of the postorder array as the root node.
// 2. Find the index of the root node in the inorder array.
// 3. Divide the inorder array into left and right subtrees based on the index of the root node.
// 4. Divide the postorder array into left and right subtrees based on the number of elements
//  in the left and right subtrees of the inorder array.
// 5. Recursively construct the left and right subtrees.

// Complexity:
// Time complexity:
// The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
// We visit each node only once.
//
//Space complexity:
// The space complexity of this algorithm is O(n). We create a hashmap to store the indices of the inorder traversal,
// which takes O(n) space. Additionally, the recursive call stack can go up to O(n) in the worst case if the binary
// tree is skewed.