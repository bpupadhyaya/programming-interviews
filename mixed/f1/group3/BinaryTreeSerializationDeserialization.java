// Serialization is the process of converting a data structure or object into a sequence of bits so that
// it can be stored in a file or memory buffer, or transmitted across a network connection link to be
// reconstructed later in the same or another computer environment.
//
//Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
// serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
// serialized to a string and this string can be deserialized to the original tree structure.
// Sample 1:
// Input: root = [1,2,3,null,null,4,5]
// Output: [1,2,3,null,null,4,5]

import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;

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
class BinaryTreeSerializationDeserialization {

    private static final String SPLITTER = ",";
    private static final String NULL_NODE = "X";
    public static void main(String...args) {
        Tree myTree = new Tree(1);
        Tree leftTree = new Tree(2);
        myTree.setLeft(leftTree);
        Tree rightTree = new Tree(3);
        rightTree.setLeft(new Tree(4));
        rightTree.setRight(new Tree(5));
        myTree.setRight(rightTree);

        String serializationResult = serialize(myTree);
        System.out.println("Serialization result: " + serializationResult);
        Tree deserializationResult = deserialize(serializationResult);
        System.out.println("Tree root: " + deserializationResult.value);
        System.out.println("Tree left: " + deserializationResult.left.value);
        System.out.println("Tree right root: " + deserializationResult.right.value);
        System.out.println("Tree right - > left : " + deserializationResult.right.left.value);
        System.out.println("Tree right - > right : " + deserializationResult.right.right.value);
    }

    static String serialize(Tree tree) {
        StringBuilder sb = new StringBuilder();
        buildString(tree, sb);

        return sb.toString();
    }

    private static void buildString(Tree tree, StringBuilder sb) {
        if (tree == null) {
            sb.append(NULL_NODE).append(SPLITTER);
        } else {
            sb.append(tree.value).append(SPLITTER);
            buildString(tree.left, sb);
            buildString(tree.right, sb);
        }
    }

    static Tree deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(SPLITTER)));
        return buildTree(nodes);
    }

    private static Tree buildTree(Deque<String> nodes) {
        String val = nodes.remove();
        if (val.equals(NULL_NODE))
            return null;
        else {
            Tree tree = new Tree(Integer.valueOf(val));
            tree.left = buildTree(nodes);
            tree.right = buildTree(nodes);

            return tree;
        }
    }
}