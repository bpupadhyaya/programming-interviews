// Given the head of a linked list, return the list after sorting it in ascending order.
// Example:
// Input: head = [4,2,1,3]
// Output: [1,2,3,4]
//
// Tag: 109/150
// Tag: 148/2927, R564/2936 (overall frequency ranking)


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
class SortedList {
    public static void main(String...args) {
        int[] headArray = {4, 2, 1, 3};
        ListNode head = new ListNode(4, new ListNode(2));
        head.next.next = new ListNode(1);
        head.next.next.next = new ListNode(3);
        ListNode sHead = sortList(head);
        System.out.print(sHead.val + "," + sHead.next.val + "," + sHead.next.next.val + "," + sHead.next.next.next.val);
        System.out.println();
    }

    static ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        // 1. Split the list into two halves
        ListNode prev = null, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;

        // 2. Sort each half
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);

        // 3. Merge l1 and l2
        return merge(l1, l2);
    }

    private static ListNode merge(ListNode l1, ListNode l2) {
        ListNode l = new ListNode(0), p = l;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        if (l1 != null)
            p.next = l1;
        if (l2 != null)
            p.next = l2;

        return l.next;
    }
}
