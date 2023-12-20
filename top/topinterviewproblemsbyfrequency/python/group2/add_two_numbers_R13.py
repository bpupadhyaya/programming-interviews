"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Tag: R13/145
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    d = n = ListNode(0)
    num1 = num2 = ""
    while l1:
        num1 += str(l1.val)
        l1 = l1.next
    while l2:
        num2 += str(l2.val)
        l2 = l2.next
    res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
    for i in res:
        d.next = ListNode(i)
        d = d.next
    return n.next


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = add_two_numbers(l1, l2)
    print(res.val, res.next.val, res.next.next.val)


if __name__ == "__main__":
    main()
