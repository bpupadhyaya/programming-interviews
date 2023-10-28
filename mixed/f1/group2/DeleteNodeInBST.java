// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node
// reference (possibly updated) of the BST.
// Basically, the deletion can be divided into two stages:
// Search for a node to remove.
// If the node is found, delete the node.
// Sample 1:
// Input: root = [5,3,6,2,4,null,7], key = 3
// Output: [5,4,6,2,null,null,7]
// Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
// One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
// Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
// Visualize to understand

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
class DeleteNodeInBST {
    public static void main(String...args) {
        TreeNode root = new TreeNode(5, new TreeNode(3),new TreeNode(6));
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(4);
        root.right.right = new TreeNode(7);

        int key = 3;
        TreeNode finalTree = deleteNode(root, key);
        System.out.print(finalTree.val + ",");
        System.out.print(finalTree.left.val + ",");
        System.out.print(finalTree.left.left.val + ",");
        System.out.print(finalTree.right.val + ",");
        System.out.print(finalTree.right.right.val);
        System.out.println();
    }

    static TreeNode deleteNode(TreeNode root, int key) {
        if (root == null)
            return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key);
            return root;
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
            return root;
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            } else {
                TreeNode min = root.right;
                while (min.left != null) {
                    min = min.left;
                }

                root.val = min.val;
                root.right = deleteNode(root.right, min.val);
                return root;
            }
        }
    }
}
