// Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
// Sample 1:
// Input: head = [1,2,2,1]
// Output: true
// Note: Visualize to understand: 1 -> 2 -> 2-> 1

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

class PalindromeLinkedList {
    public static void main(String...args) {
        ListNode head = new ListNode(1, new ListNode(2));
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(1);

        System.out.println("Palindrome? " + isPalindrome(head));
    }

    static boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head, prev, temp;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        prev = slow;
        slow = slow.next;
        prev.next = null;
        while (slow != null) {
            temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        fast = head;
        slow = prev;
        while (slow != null) {
            if (fast.val != slow.val)
                return false;
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
}