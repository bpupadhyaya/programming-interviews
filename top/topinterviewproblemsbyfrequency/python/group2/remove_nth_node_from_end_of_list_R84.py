"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Sample 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Tag: R84/145
Tag: 63/150
Tag: 19/2927, R286/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head
    # Advance fast to nth position
    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next
    # Then advance both fast and slow now they are nth position apart
    # When fast goes to None, slow will be just before the item to be deleted
    while fast.next:
        slow = slow.next
        fast = fast.next
    # Delete the node
    slow.next = slow.next.next
    return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2

    res = remove_nth_from_end(head, n)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val)


if __name__ == "__main__":
    main()
