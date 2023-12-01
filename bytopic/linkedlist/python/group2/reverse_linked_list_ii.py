"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the
nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Tag: 61/150
Tag: 92/2927, R306/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between_using_two_pointer(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head
    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next

    for _ in range(right - left):
        next_node = current.next
        current.next, next_node.next, prev.next = next_node.next, prev.next, next_node
    return dummy.next


def reverse_between_using_recursion(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not (head and left < right):
        return head

    def helper(node, m):
        nonlocal left, right
        if m == left:
            prev = None
            current = node
            while m <= right:
                current.next, prev, current = prev, current, current.next
                m += 1
            node.next = current
            return prev
        elif m < left:
            node.next = helper(node.next, m + 1)
        return node
    return helper(head, 1)


def reverse_between_using_stack(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    stack = []
    current = prev.next

    for _ in range(right - left + 1):
        stack.append(current)
        current = current.next

    while stack:
        prev.next = stack.pop()
        prev = prev.next

    prev.next = current

    return dummy.next


def main():
    left = 2
    right = 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    res = reverse_between_using_stack(head, left, right)
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val)


if __name__ == "__main__":
    main()
