"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Tag: 66/150
Tag: 86/2927, R353/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before, after = ListNode(0), ListNode(0)
    before_curr, after_curr = before, after

    while head:
        if head.val < x:
            before_curr.next, before_curr = head, head
        else:
            after_curr.next, after_curr = head, head
        head = head.next

    after_curr.next = None
    before_curr.next = after.next

    return before.next


def main():
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3
    res = partition(head, x)

    while res.next is not None:
        print(res.val, end=", ")
        res = res.next
    print(res.val)  # last value


if __name__ == "__main__":
    main()
