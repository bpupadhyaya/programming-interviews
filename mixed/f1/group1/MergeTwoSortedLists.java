// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the
// first two lists. Return the head of the merged linked list.
// Sample 1:
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
class MergeTwoSortedLists {
    public static void main(String...args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(4);

        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        ListNode merged = mergeTwoSortedLists(list1, list2);
        System.out.print(merged.val+", ");
        System.out.print(merged.next.val+", ");
        System.out.print(merged.next.next.val+", ");
        System.out.print(merged.next.next.next.val+", ");
        System.out.print(merged.next.next.next.next.val+", ");
        System.out.println(merged.next.next.next.next.val);
    }

    static ListNode mergeTwoSortedLists(ListNode list1, ListNode list2) {
        if (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                list1.next = mergeTwoSortedLists(list1.next, list2);
                return list1;
            } else {
                list2.next = mergeTwoSortedLists(list1, list2.next);
                return list2;
            }
        }
        if (list1 == null)
            return list2;

        return list1;
    }
}