// A linked list of length n is given such that each node contains an additional random pointer, which could
// point to any node in the list, or null.
// Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each
// new node has its value set to the value of its corresponding original node. Both the next and random pointer
// of the new nodes should point to new nodes in the copied list such that the pointers in the original list
// and copied list represent the same list state. None of the pointers in the new list should point to nodes
// in the original list.
// For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the
// corresponding two nodes x and y in the copied list, x.random --> y.
// Return the head of the copied linked list.
// The linked list is represented in the input/output as a list of n nodes. Each node is represented as a
// pair of [val, random_index] where:
// val: an integer representing Node.val
// random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it
// does not point to any node.
// Your code will only be given the head of the original linked list.
// Sample 1:
// Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Note: the second value in the list is the index this node is pointing to. The first values are linked as
// regular linked list, eg 7 points to 13 as its next, 13 points to 11 as its next and so on.
// Note: Elements are copied but random pointers didn't get printed, debug and fix.

import java.util.HashMap;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
class CopyListWithRandomPointer {
    public static void main(String...args) {
        Node ll = new Node(7);
        ll.random = null;
        ll.next = new Node(13);
        ll.next.random = new Node(0);
        ll.next.next = new Node(11);
        ll.next.next.random = new Node(4);
        ll.next.next.next = new Node(10);
        ll.next.next.next.random = new Node(2);
        ll.next.next.next.next = new Node(1);
        ll.next.next.next.next.random = new Node(0);

        Node copiedList = copyRandomPointerList(ll);
        Node curr = copiedList;
        while (curr != null) {
            System.out.print("[");
            System.out.print(curr.val + ",");
            if (curr.random != null) {
                System.out.print(curr.random.val + ",");
            }
            System.out.print("]");
            curr = curr.next;
        }
        System.out.println();
    }

    static Node copyRandomPointerList(Node head) {
        if (head == null) {
            return null;
        }

        HashMap<Node, Node> oldToNew = new HashMap<>();
        Node curr = head;
        while (curr != null) {
            oldToNew.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;
        while (curr != null) {
            oldToNew.get(curr).next = oldToNew.get(curr.next);
            oldToNew.get(curr).random = oldToNew.get(curr.random);
            curr = curr.next;
        }

        return oldToNew.get(head);
    }
}