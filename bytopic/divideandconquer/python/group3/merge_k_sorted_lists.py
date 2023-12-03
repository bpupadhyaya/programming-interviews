"""
 Given an array of k linked lists that are sorted in ascending order, merge all the linked lists
into one sorted linked list and return it.

Sample 1:
Input lists = [[11, 14, 16],[11, 12, 18],[13,15]]
Output: [11, 11,12,13,14,15,16,18]

Tag: 111/150
Tag: 23/2927, R145/2936 (overall frequency ranking)
"""
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    h = []
    head = tail = ListNode(0)
    for i in range(len(lists)):
        heapq.heappush(h, (lists[i].val, i, lists[i]))

    while h:
        node = heapq.heappop(h)
        node = node[2]
        tail.next = node
        tail = tail.next
        if node.next:
            i += 1
            heapq.heappush(h, (node.next.val, i, node.next))

    return head.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    ListNode.__lt__ = lambda self, other: self.val < other.val
    h = []
    head = tail = ListNode(0)
    for i in lists:
        if i:
            heapq.heappush(h, (i.val, i))
    while h:
        node = heapq.heappop(h)[1]
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(h, (node.next.val, node.next))
    return head.next


def main():
    head1 = ListNode(11)
    head1.next = ListNode(14)
    head1.next.next = ListNode(16)
    head2 = ListNode(11)
    head2.next = ListNode(12)
    head2.next.next = ListNode(18)
    head3 = ListNode(13)
    head3.next = ListNode(15)

    res = merge_k_lists_1([head1, head2, head3])
    while res is not None:
        print(res.val, end=",")
        res = res.next


if __name__ == "__main__":
    main()
