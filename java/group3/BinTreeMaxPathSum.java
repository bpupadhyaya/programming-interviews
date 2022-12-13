// Find the maximum path sum of any non-empty path of a given binary tree.
// Soln: Time complexity: O(n), space complexity: O(n)

class Tree {
    int value;
    Tree left;
    Tree right;
    Tree(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
    Tree(int value, Tree left, Tree right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
    public int getValue() {
        return this.value;
    }
    public void setValue(int value) {
        this.value = value;
    }
    public Tree getLeft() {
        return this.left;
    }
    public void setLeft(Tree left) {
        this.left = left;
    }
    public Tree getRight() {
        return this.right;
    }
    public void setRight(Tree right) {
        this.right = right;
    }

}

class BinTreeMaxPathSum {

    public static void main(String...args) {
        Tree l12 = new Tree(25);
        Tree l1 = new Tree(4,null,l12);
        Tree r11 = new Tree(8);
        Tree r1 = new Tree(7, null, r11);
        Tree tree = new Tree(5, l1, r1);

        System.out.println("Max path sum: " + findMaxPathSum(tree));
    }

    private static int findMaxPathSum(Tree root) {
        return navigateSubTree(root);
    }

    private static int navigateSubTree(Tree root) {

        if (root == null) {
            return 0;
        }

        int leftG = Math.max(navigateSubTree(root.left), 0);
        int rightG = Math.max(navigateSubTree(root.right), 0);

        return Math.max(leftG + root.value, rightG + root.value);
    }

}