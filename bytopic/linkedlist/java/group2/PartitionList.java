// Given the head of a linked list and a value x, partition it such that all nodes less than x come before
// nodes greater than or equal to x.
// You should preserve the original relative order of the nodes in each of the two partitions.
// Example:
// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]
//
// Tag: 66/150
// Tag: 86/2927, R353/2936 (overall frequency ranking)

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

class ListPartitioning {
    public static void main(String...args) {
        ListNode list = new ListNode(1);
        list.next = new ListNode(4);
        list.next.next = new ListNode(3);
        list.next.next.next = new ListNode(2);
        list.next.next.next.next = new ListNode(5);
        list.next.next.next.next.next = new ListNode(2);
        int x = 3;

        ListNode result = partition(list, x);
        while (result.next != null) {
            System.out.print(result.value + ",");
            result = result.next;
        }
        System.out.print(result.value); // Last value
        System.out.println();
    }

    static ListNode partition(ListNode head, int x) {
        ListNode before = new ListNode(0);
        ListNode after = new ListNode(0);
        ListNode beforeCurr = before;
        ListNode afterCurr = after;

        while (head != null) {
            if (head.value < x) {
                beforeCurr.next = head;
                beforeCurr = beforeCurr.next;
            } else {
                afterCurr.next = head;
                afterCurr = afterCurr.next;
            }
            head = head.next;
        }

        afterCurr.next = null;
        beforeCurr.next = after.next;

        return before.next;
    }
}