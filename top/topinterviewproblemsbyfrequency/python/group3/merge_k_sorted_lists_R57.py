"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.

Tag: R57/145
"""
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_python_2(lists: list[ListNode]) -> ListNode:
    # Doesn't work with Python3 interpreter, need to implement __eq__ and __lt__
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


def merge_k_lists_python_3(lists: list[ListNode]) -> ListNode:
    # Needs debugging for full output
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


def merge_k_lists_using_fix_heapq(lists: list[ListNode]) -> ListNode:
    # Needs debugging
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
            heapq.heappush(h, (node.next.val, i. node.next))
    return head.next


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    # Debug
    v = []
    for i in lists:
        x = i
        while x:
            v += [x.val]
            x = x.next
        v = sorted(v, reverse=True)
        ans = None
        for i in v:
            ans = ListNode(i, ans)
        return ans


def merge_k_lists_1(lists: list[ListNode]) -> ListNode:
    # Some values are missing in the output, debug and fix
    head = ListNode(None)
    curr = head
    h = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next

    while h:
        val, i = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next

    return head.next


def main():
    # Input: lists = [[1,4,5],[1,3,4],[2,6]]
    # Output: [1,1,2,3,4,4,5,6]
    l1 = ListNode(1, ListNode(4))
    l1.next = ListNode(5)
    l2 = ListNode(1, ListNode(3))
    l2.next = ListNode(4)
    l3 = ListNode(2, ListNode(6))

    l4 = merge_k_lists_1([l1, l2, l3])
    print(l4.val, l4.next.val, l4.next.next.val, l4.next.next.next.val, l4.next.next.next.next.val,
          l4.next.next.next.next.next.val, l4.next.next.next.next.next.next.val,
          l4.next.next.next.next.next.next.next.val)


if __name__ == "__main__":
    main()
