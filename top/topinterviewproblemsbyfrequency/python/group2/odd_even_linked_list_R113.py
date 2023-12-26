"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with
even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6

R113/145
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: ListNode) -> ListNode:
    if not head:
        return None
    # odd points to the first node
    odd = head
    # even points to the second node
    # even_head will be used at the end to connect odd and even nodes
    even_head = even = head.next

    # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
    # If even is not None, then odd is not None. (odd before even)
    # If even.next is not None, then after we update odd to the next odd node, it cannot be None. (The next odd node
    # is even.next)
    while even and even.next:
        # Connect the current odd node to the next odd node
        odd.next = odd.next.next
        # Move the current odd node to the next odd node
        odd = odd.next
        # Same thing for even node
        even.next = even.next.next
        even = even.next

    # Connect the last odd node to the start of the even node
    odd.next = even_head

    # head never changed, so return it
    return head


def main():
    # head = [1,2,3,4,5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    res = odd_even_list(head)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)


if __name__ == "__main__":
    main()


"""
Implementation note:
The problem needs to be solved with O(1) space, which leaves us no other choice but to try to use pointers to 
reorganize the linked list.
(1) We use a odd pointer to link all the odd-positioned nodes, and a even pointer to link all the even-positioned nodes.
(2) We connect the two linked lists at the end, i.e., connect the last node in the odd list to the first node in
 the even list.

A few things we need to take care of:

There is a pointer that always points to the first node of the original linked list so we can return it (This is
 easy, just don't change head at all).
There is a pointer that always points to the second node of the original linked list so that, in the end, we
 can connect the last odd node to it. (This is also easy, just create evenHead points to the second node at
  the beginning)
After the iteration of connecting odd nodes to odd nodes and even nodes to even nodes, the odd pointer has
 to point to the last odd node (so we can connect it to evenHead).
"""
