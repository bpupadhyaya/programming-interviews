// Given the root of a binary tree, return all paths from root, traversal order is not important.

import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class BinaryTreePath {
    public static void main(String...args) {
        TreeNode r14 = new TreeNode(14,null, null);
        TreeNode r12 = new TreeNode(12,null, null);
        TreeNode l10 = new TreeNode(10,null, r14);
        TreeNode root = new TreeNode(4, l10, r12);

        LinkedList<String> paths = new LinkedList<>();
        String pathSt = "";
        paths = constructPaths(root, paths, pathSt);
        System.out.println(paths);
    }

    private static LinkedList<String> constructPaths(TreeNode root, LinkedList<String> paths, String pathSt) {
        if (root != null) {
            pathSt += Integer.toString(root.val);
            if((root.left == null) && (root.right == null)) {
                paths.add(pathSt);
            } else {
              pathSt += "->";
              constructPaths(root.left, paths, pathSt);
              constructPaths(root.right, paths, pathSt);
            }
        }
        return paths;
    }
}