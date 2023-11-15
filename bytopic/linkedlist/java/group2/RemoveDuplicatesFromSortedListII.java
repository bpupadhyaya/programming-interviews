// Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only
// distinct numbers from the original list. Return the linked list sorted as well.
// Example :
// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]
//
// Tag: 64/150
// Tag: 82/2927, R918/2936 (overall frequency ranking)

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

class RemovalOfDuplicatesFromSortedListII {
    public static void main(String[] args) {
        ListNode list = new ListNode(1);
        list.next = new ListNode(2);
        list.next.next = new ListNode(3);
        list.next.next.next = new ListNode(3);
        list.next.next.next.next = new ListNode(4);
        list.next.next.next.next.next = new ListNode(4);
        list.next.next.next.next.next.next = new ListNode(5);

        ListNode result = deleteDuplicates(list);
        while (result.next != null) {
            System.out.print(result.value + ",");
            result = result.next;
        }
        System.out.print(result.value); // Last value
        System.out.println();
    }

    static ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;

        while (curr.next != null && curr.next.next != null) {
            if (curr.next.value == curr.next.next.value) {
                int duplicate = curr.next.value;
                while (curr.next != null && curr.next.value == duplicate) {
                    curr.next = curr.next.next;
                }
            } else {
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}

