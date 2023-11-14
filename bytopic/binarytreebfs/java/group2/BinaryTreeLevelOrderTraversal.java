// Given the root of a binary tree, return the level order traversal of its nodes' values.
// (i.e., from left to right, level by level).
// Sample 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
// Note: visualize to understand
// It is row level traversal starting from first row, which is root node.
// Note: some output is missing, debug and find out.
//
// Tag: 84/150
// Tag: 102/2927, R516/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;

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
class BinaryTreeLevelOrderTraversal {
    public static void main(String...args) {
        TreeNode tree = new TreeNode(3);
        TreeNode left = new TreeNode(9);
        TreeNode right = new TreeNode(20, new TreeNode(15), new TreeNode(7));
        tree.left = left;
        tree.right = right;

        List<List<Integer>> lOrder = levelOrder(tree);
        for (List<Integer> elem: lOrder) {
            System.out.print(elem + ", ");
        }
        System.out.println();
    }

    static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> myList = new ArrayList<>();
        preOrder(root, 0, myList);

        return myList;
    }

    private static void preOrder(TreeNode root, int l, List<List<Integer>> myList) {
        if (root ==  null)
            return;
        if (myList.size() == l) {
            List<Integer> list = new ArrayList<>();
            list.add(root.val);
            myList.add(list);
        } else {
            myList.get(l).add(root.val);
            preOrder(root.left, l+1, myList);
            preOrder(root.right, l+1, myList);
        }
    }
}