// Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
// BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
// constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
// boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
// int next() Moves the pointer to the right, then returns the number at the pointer.
// Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
// smallest element in the BST.
// You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
// traversal when next() is called.
// Sample 1:
// Input
// ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
// [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
// Output
// [null, 3, 7, true, 9, true, 15, true, 20, false]
// Explanation
// BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
// bSTIterator.next();    // return 3
// bSTIterator.next();    // return 7
// bSTIterator.hasNext(); // return True
// bSTIterator.next();    // return 9
// bSTIterator.hasNext(); // return True
// bSTIterator.next();    // return 15
// bSTIterator.hasNext(); // return True
// bSTIterator.next();    // return 20
// bSTIterator.hasNext(); // return False
// Note: visualize to understand
//
// Tag: 79/150
// Tag: 173/2927, R797/2936 (overall frequency ranking)

import java.util.Stack;
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

class BinarySearchTreeIterator {
    static Stack<TreeNode> stack;
    public BinarySearchTreeIterator(TreeNode root) {
        stack = new Stack<>();
        TreeNode node = root;
        updateStack(node);
    }
    public static void main(String...args) {
        TreeNode left = new TreeNode(3);
        TreeNode right = new TreeNode(15, new TreeNode(9), new TreeNode(20));
        TreeNode tree = new TreeNode(7, left, right);

        BinarySearchTreeIterator bstIter = new BinarySearchTreeIterator(tree);
        System.out.println(bstIter.next());    // return 3
        System.out.println(bstIter.next());    // return 7
        System.out.println(bstIter.hasNext()); // return True
        System.out.println(bstIter.next());    // return 9
        System.out.println(bstIter.hasNext()); // return True
        System.out.println(bstIter.next());    // return 15
        System.out.println(bstIter.hasNext()); // return True
        System.out.println(bstIter.next());    // return 20
        System.out.println(bstIter.hasNext()); // return False


    }

    public static int next() {
        TreeNode toRemove = stack.pop();
        updateStack(toRemove.right);
        return toRemove.val;
    }

    public static boolean hasNext() {
        return !stack.isEmpty();
    }

    private static void updateStack(TreeNode node) {
        while(node != null) {
            stack.add(node);
            node = node.left;
        }
    }

}