// Given the head of a linked list, rotate the list to the right by k places.
// Example:
// Input: head = [1,2,3,4,5], k = 2
// Output: [4,5,1,2,3]
//
// Tag: 65/150
// Tag: 61/2927, R401/2936 (overall frequency ranking)

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

class RotateList {
    public static void main(String...args) {
        // head = [1,2,3,4,5], k = 2
        ListNode list = new ListNode(1);
        list.next = new ListNode(2);
        list.next.next = new ListNode(3);
        list.next.next.next = new ListNode(4);
        list.next.next.next.next = new ListNode(5);
        int k = 2;

        ListNode result = rotateRight(list, k);
        while (result.next != null) {
            System.out.print(result.value + ",");
            result = result.next;
        }
        System.out.println(result.value); // Last value
        System.out.println();
    }

    static ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0)
            return head;
        ListNode temp = head;
        int count = 1;
        while (temp.next != null) {
            count++;
            temp = temp.next;
        }
        temp.next = head;
        k = k % count;
        k = count - k;
        while (k != 0) {
            temp = temp.next;
            k--;
        }
        head = temp.next;
        temp.next = null;

        return head;
    }
}

// Method:
// we calculate the length of the linked list and after reaching the last node of the linked list we point its next
// to head making it a circular linked list. And then we forward temp k places ahead and set the head value to
// temp.next and then set temp.next to null. Thus, rotating the linked list to the right by k places.