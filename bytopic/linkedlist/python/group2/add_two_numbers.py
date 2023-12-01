"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Tag: 58/150
Tag: 2/2927, R16/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    tail = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        sum_ = digit1 + digit2 + carry
        digit = sum_ % 10
        carry = sum_ // 10

        new_node = ListNode(digit)
        tail.next = new_node
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = dummy_head.next
    dummy_head.next = None
    return result


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = add_two_numbers(l1, l2)
    print(res.val, res.next.val, res.next.next.val)


if __name__ == "__main__":
    main()
