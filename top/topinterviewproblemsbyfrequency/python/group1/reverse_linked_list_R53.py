"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Note: Visualize to understand

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Tag: R53/145
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def main():
    head = ListNode(1, ListNode(2))
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    res = reverse_list(head)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)


if __name__ == "__main__":
    main()
