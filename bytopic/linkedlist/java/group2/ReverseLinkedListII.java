// Given the head of a singly linked list and two integers left and right where left <= right, reverse the
// nodes of the list from position left to position right, and return the reversed list.
// Sample 1:
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
//
// Tag: 61/150
// Tag: 92/2927

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
class ReverseLinkedListII {
    public static void main(String...args) {
        ListNode ll = new ListNode(1);
        ll.next = new ListNode(2);
        ll.next.next = new ListNode(3);
        ll.next.next.next = new ListNode(4);
        ll.next.next.next.next = new ListNode(5);
        int left = 2;
        int right = 4;
        ListNode revLl = reverseLinkedList(ll, left, right);
        System.out.print(revLl.value + ", ");
        System.out.print(revLl.next.value + ", ");
        System.out.print(revLl.next.next.value + ", ");
        System.out.print(revLl.next.next.next.value + ", ");
        System.out.print(revLl.next.next.next.next.value);
        System.out.println();
    }

    static ListNode reverseLinkedList(ListNode head, int left, int right) {
        ListNode temp = new ListNode(0);
        temp.next = head;
        ListNode prev = temp;
        for (int i = 0; i < left - 1; i++)
            prev = prev.next;
        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode forw = curr.next;
            curr.next = forw.next;
            forw.next = prev.next;
            prev.next = forw;
        }
        return temp.next;
    }
}