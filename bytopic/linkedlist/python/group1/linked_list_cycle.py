"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's
next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Note: Visualize to understand

Tag: 57/150
Tag: 141/2927, R336/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle_using_hashtable(head: Optional[ListNode]) -> bool:
    dictionary = {}
    while head:
        if head in dictionary:
            return True
        else:
            dictionary[head] = True
        head = head.next
    return False


def has_cycle_using_two_pointer(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(has_cycle_using_two_pointer(head))


if __name__ == "__main__":
    main()
