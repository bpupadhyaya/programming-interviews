"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If
the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to
your program. If you correctly return the intersected node, then your solution will be accepted.

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes
before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and
3rd node in B) are different node references. In other words, they point to two different locations in memory,
 while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

R106/145
Note: both approaches need further debugging to find out problem, output is not correct
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    # Using two pointers, complexity: time: O(m+n), space: O(1)
    one = head_a
    two = head_b

    while one != two:
        one = head_b if one is None else one.next
        two = head_a if two is None else two.next
    return one


def get_intersection_node_1(head_a: ListNode, head_b: ListNode) -> ListNode:
    # Using hashset, complexity: time: O(m+n), space: O(n)
    first_set = set()
    curr = head_a

    while curr:
        first_set.add(curr)
        curr = curr.next

    curr = head_b
    while curr:
        if curr in first_set:
            return curr
        curr = curr.next

    return None


def main():
    list_a = ListNode(4)
    list_a.next = ListNode(1)
    list_a.next.next = ListNode(8)
    list_a.next.next.next = ListNode(4)
    list_a.next.next.next.next = ListNode(5)

    list_b = ListNode(5)
    list_b.next = ListNode(6)
    list_b.next.next = ListNode(1)
    list_b.next.next.next = ListNode(8)
    list_b.next.next.next.next = ListNode(4)
    list_b.next.next.next.next.next = ListNode(5)

    res = get_intersection_node_1(list_a, list_b)
    print(res.val)


if __name__ == "__main__":
    main()
