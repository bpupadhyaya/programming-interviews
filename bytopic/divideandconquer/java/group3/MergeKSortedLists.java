//  Given an array of k linked lists that are sorted in ascending order, merge all the linked lists
// into one sorted linked list and return it.
// Sample 1:
// Input lists = [[11, 14, 16],[11, 12, 18],[13,15]]
// Output: [11,12,13,14,15,16,18]
//
// Tag: 111/150
// Tag: 23/2927, R145/2936 (overall frequency ranking)

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
class MergeKSortedLists {
    public static void main(String...args) {
        ListNode l1 = new ListNode(11);
        l1.next = new ListNode(14);
        l1.next.next = new ListNode(16);

        ListNode l2 = new ListNode(11);
        l2.next = new ListNode(12);
        l2.next.next = new ListNode(18);

        ListNode l3 = new ListNode(13);
        l3.next = new ListNode(15);

        ListNode[] lists = {l1, l2, l3};


        ListNode result = mergeKSortedLists(lists);
        while (result != null) {
            System.out.printf(result.value +", ");
            result = result.next;
        }
        System.out.println();

    }

    static ListNode mergeKSortedLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        return mergeKSortedListsHelper(lists, 0, lists.length - 1);
    }

    static ListNode mergeKSortedListsHelper(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        }
        if (start + 1 == end) {
            return merge(lists[start], lists[end]);
        }

        int mid = start + (end - start) / 2;
        ListNode left = mergeKSortedListsHelper(lists, start, mid);
        ListNode right = mergeKSortedListsHelper(lists, mid + 1, end);
        return merge(left, right);
    }

    static ListNode merge(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0);
        ListNode curr = temp;

        while(l1 != null && l2 != null) {
            if (l1.value < l2.value) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return temp.next;
    }
}