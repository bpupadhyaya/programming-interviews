"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list. Return the linked list sorted as well.

Example :
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Tag: 64/150
Tag: 82/2927, R918/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            prev.next = head
        else:
            prev = prev.next
            head = head.next
    return dummy.next


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    res = delete_duplicates(head)
    print(res.val, res.next.val, res.next.next.val)


if __name__ == "__main__":
    main()

