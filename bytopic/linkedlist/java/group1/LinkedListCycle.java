// Given head, the head of a linked list, determine if the linked list has a cycle in it.
// There is a cycle in a linked list if there is some node in the list that can be reached again by
// continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's
// next pointer is connected to. Note that pos is not passed as a parameter.
// Return true if there is a cycle in the linked list. Otherwise, return false.
// Input: head = [1], pos = -1
// Output: false
// Explanation: There is no cycle in the linked list.
// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
// Note: Visualize to understand
//
// Tag: 57/150
// Tag: 141/2927

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

class LinkedListCycle {
    public static void main(String[] args) {
        ListNode list = new ListNode(3);
        list.next = new ListNode(2);
        list.next.next = new ListNode(0);
        list.next.next.next = new ListNode(-4);
        list.next.next.next = list.next; // pos = 1

        System.out.println("Has cycle? " + hasCycle(list));
    }

    static boolean hasCycle(ListNode head) {
        ListNode slowPointer = head;
        ListNode fastPointer = head;
        while (fastPointer != null && fastPointer.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
            if (slowPointer == fastPointer)
                return true;
        }
        return false;
    }
}

// Verify this:
// Two-Pointers Method (Floyd's Cycle-Finding Algorithm):
// Also known as the "hare and tortoise" algorithm, this method employs two pointers that move at different speeds.
// If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's
// existence.
