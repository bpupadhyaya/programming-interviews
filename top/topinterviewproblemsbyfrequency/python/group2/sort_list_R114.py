"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Tag: R114/145
Tag: 109/150
Tag: 148/2927, R564/2936 (overall frequency ranking)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list_using_bubble_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    count = head
    while count:
        itr = head
        while itr.next:
            if itr.val > itr.next.val:
                itr.val, itr.next.val = itr.next.val, itr.val
            itr = itr.next
        count = count.next
    return head


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
    if not head or not head.next:
        return head

    # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint
    # of the linked list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # The midpoint of the linked list is slow.next
    mid = slow.next
    # Set slow.next to None to separate the left and right halves of the linked list
    slow.next = None

    # Recursively sort the left and right halves of the linked list
    left = sort_list(head)
    right = sort_list(mid)

    # Merge the two sorted halves of the linked list
    dummy = ListNode(0)
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    # Append the remaining nodes of the left or right half to the end of the sorted list
    curr.next = left or right

    return dummy.next


def main():
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    res = sort_list(head)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val)


if __name__ == "__main__":
    main()
