// Given the head of a linked list, remove the nth node from the end of the list and return its head.
// Sample 1:
// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Note: Needs fix in printing values, probably more.


class ListNode {
    int value;
    ListNode next;

    public ListNode(int value) {
        this.value = value;
    }
    public ListNode(int value, ListNode next) {
        this.value = value;
        this.next = next;
    }
}
class RemoveNthNodeFromEndOfList {
    public static void main(String...args) {
        ListNode myNode = new ListNode(1);
        myNode.next = new ListNode(2);
        myNode.next = new ListNode(3);
        myNode.next = new ListNode(4);
        myNode.next = new ListNode(5);

        int n = 2;
        ListNode output = removeNthNodeFromEndOfList(myNode, n);
        System.out.println(output.value);
        System.out.println(output.next.value);
        System.out.println(output.next.next.value);
        System.out.println(output.next.next.next.value);
    }

    static ListNode removeNthNodeFromEndOfList(ListNode head, int n) {
        ListNode fast = head, slow = head;
        for (int i = 0; i < n; i++)
            fast = fast.next;
        if (fast == null)
            return head.next;
        while(fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;

        return head;
    }
}