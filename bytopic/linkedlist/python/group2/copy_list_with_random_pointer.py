"""
A linked list of length n is given such that each node contains an additional random pointer, which could
point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each
new node has its value set to the value of its corresponding original node. Both the next and random pointer
of the new nodes should point to new nodes in the copied list such that the pointers in the original list
and copied list represent the same list state. None of the pointers in the new list should point to nodes
in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the
corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a
pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it
does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Note: the second value in the list is the index this node is pointing to. The first values are linked as
regular linked list, eg 7 points to 13 as its next, 13 points to 11 as its next and so on.
Note: Elements are copied but random pointers didn't get printed, debug and fix.

Tag: 60/150
Tag: 138/2927, R116/2936 (overall frequency ranking), fb R8/50
Note: currently output prints node value for random pointer node, instead of index.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    old_to_new = {}

    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]


def main():
    head = Node(7, Node(13), None)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    res = copy_random_list(head)

    print(res.val, None)
    print(res.next.val, res.next.random.val)
    print(res.next.next.val, res.next.next.random.val)
    print(res.next.next.next.val, res.next.next.next.random.val)
    print(res.next.next.next.next.val, res.next.next.next.next.random.val)


if __name__ == "__main__":
    main()
