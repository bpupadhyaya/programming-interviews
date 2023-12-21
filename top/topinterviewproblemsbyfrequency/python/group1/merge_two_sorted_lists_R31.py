"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Tag: R31/145
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    res = merge_two_lists(list1, list2)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val,
          res.next.next.next.next.val)


if __name__ == "__main__":
    main()


"""
For simplicity, we create a dummy node to which we attach nodes from lists. We iterate over lists using two-pointers 
and build up a resulting list so that values are monotonically increased.

Complexity:
Time: O(n)
Space: O(1)
"""
