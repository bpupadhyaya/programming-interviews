// Given two non-empty linked lists containing digits of a number each stored in reverse order,
// add two numbers.
// Sample input: ll1 = [2,3,1], ll2 = [5,7,1]
// Sample output: [7,0,3]

class Node {
    int value;
    Node next;
    Node () {}
    Node(int value) {this.value = value;}
    Node(int value, Node next) {this.value = value; this.next = next;}

}

class AddNumLinkedList {
    public static void main(String[] args) {
        Node n1 = new Node(2);
        Node n11 = new Node(3);
        Node n111 = new Node(1);
        n1.next = n11;
        n11.next = n111;
        Node n2 = new Node(1);
        Node n21 = new Node(7);
        Node n211 = new Node(5);
        n2.next = n21;
        n21.next = n211;
        Node sum = addNum(n1, n2);
        System.out.print(sum.value + "," + sum.next.value + "," + sum.next.next.value);
        System.out.println();
    }

    private static Node addNum(Node n1, Node n2) {
        Node tempHead = new Node(0);
        Node curr = tempHead;
        int carry = 0;
        while (n1 != null || n2 != null || carry != 0) {
            int x = (n1 != null) ? n1.value : 0;
            int y = (n2 != null) ? n2.value : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            curr.next = new Node(sum % 10);
            curr = curr.next;
            if (n1 != null)
                n1 = n1.next;
            if (n2 != null)
                n2 = n2.next;
        }
        return tempHead.next;
    }
}