// Given an integer n, return all the structurally unique BST's (binary search trees),
// which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
// Sample 1:
// Input: n = 3
// Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
// Note: visualize to understand

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
class UniqueBinarySearchTreesII {
    public static void main(String...args) {
        int n = 3;
        List<TreeNode> trees = generateTrees(n);
        for (TreeNode tree: trees) {
            System.out.print("[");
            printBinaryTree(tree);
            System.out.print("], ");
        }
        System.out.println();
    }

    private static void printBinaryTree(TreeNode tree) {
        if (tree != null) {
            System.out.print(tree.val + ",");
            if (tree.left != null)
                printBinaryTree(tree.left);
            if (tree.right != null)
                printBinaryTree(tree.right);
        }
    }

    static List<TreeNode> generateTrees(int n) {
        return n > 0? generateTreesHelper(1, n) : new ArrayList<>();
    }

    private static List<TreeNode> generateTreesHelper(int start, int end) {
        List<TreeNode> allTrees = new ArrayList<>();
        if (start > end) {
            allTrees.add(null);
            return allTrees;
        }

        for (int i = start; i <= end; i++) {
            List<TreeNode> leftTrees = generateTreesHelper(start, i-1);
            List<TreeNode> rightTrees = generateTreesHelper(i+1, end);

            for (TreeNode l: leftTrees) {
                for (TreeNode r: rightTrees) {
                    TreeNode currentTree = new TreeNode(i);
                    currentTree.left = l;
                    currentTree.right = r;
                    allTrees.add(currentTree);
                }
            }
        }

        return allTrees;
    }
}
