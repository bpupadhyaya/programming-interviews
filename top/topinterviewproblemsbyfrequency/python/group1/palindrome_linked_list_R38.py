"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example:
Input: head = [1,2,2,1]
Output: true

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

Tag: R38/145
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    slow = fast = head
    reversed_list = None
    # Reverse left half of the list while searching
    # the starting point of the right half
    while fast is not None and fast.next is not None:
        tmp = slow
        # Keep moving
        slow = slow.next
        fast = fast.next.next
        # Place node at the start of the reversed half
        tmp.next = reversed_list
        reversed_list = tmp
    # If there are even number of elements in the list
    # do one more step to reach the first element of
    # the second list's half
    if fast is not None:
        slow = slow.next
    # Compare reversed left half with the original
    # right half
    while reversed_list is not None and reversed_list.val == slow.val:
        reversed_list = reversed_list.next
        slow = slow.next
    return reversed_list is None


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(is_palindrome(head))


if __name__ == "__main__":
    main()


"""
Complexity:
Time complexity: O(n). We make the same number of iterations as there are nodes in the list.
Space complexity: O(1). We have not created any additional nodes and all operations were made in-place.
"""
