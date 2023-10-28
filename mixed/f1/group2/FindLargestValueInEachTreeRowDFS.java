// Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
// Sample 1:
// Input: root = [1,3,2,5,3,null,9]
// Output: [1,3,9]
// Note: visualize to understand
// Soln: DFS
// TC: O(n)
// SC: O(n)

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
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
class FindLargestValueInEachTreeRowDFS {
    public static void main(String...args) {
        TreeNode root = new TreeNode(1, new TreeNode(3), new TreeNode(2));
        root.left.left = new TreeNode(5);
        root.left.right = new TreeNode(3);
        root.right.right = new TreeNode(9);

        List<Integer> largestValues = largestValues(root);
        System.out.println("Largest values: " + largestValues);
    }

    static List<Integer> largestValues(TreeNode root) {
        Map<Integer, Integer> map = new HashMap<>();
        dfs(root, 0, map);
        return new ArrayList(map.values());
    }

    private static void dfs(TreeNode root, int level, Map<Integer, Integer> map) {
        if (root == null)
            return;

        map.put(level, Math.max(root.val, map.getOrDefault(level, Integer.MIN_VALUE)));
        dfs(root.left, level+1, map);
        dfs(root.right, level+1, map);
    }
}