"""
Given the head of a linked list, rotate the list to the right by k places.

Example:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Tag: 65/150
Tag: 61/2927, R401/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    last_element = head
    length = 1
    while last_element.next:
        last_element = last_element.next
        length += 1
    k = k % length
    last_element.next = head
    temp_node = head
    for _ in range(length - k - 1):
        temp_node = temp_node.next
    answer = temp_node.next
    temp_node.next = None

    return answer


def main():
    # head = [1,2,3,4,5], k = 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    res = rotate_right(head, k)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)


if __name__ == "__main__":
    main()
