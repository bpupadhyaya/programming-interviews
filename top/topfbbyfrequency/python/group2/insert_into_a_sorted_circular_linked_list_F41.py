"""
Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value
insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any
single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After
the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return
the reference to that single node. Otherwise, you should return the originally given node.

Example:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference
to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1
and node 3. After the insertion, the list should look like this (visualize), and we should still return node 3.

Tag: fb R41/50, 708/2927, R1231/2936

Note: Programs runs but produces wrong output, debug and fix it.
"""

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head: 'Optional[Node]', insert_val: int) -> 'Node':
    # edge cases
    if not head:
        node = Node(insert_val)
        node.next = node
        return node

    curr = head
    while curr.next != head:
        # insert in the normal position
        if curr.val <= insert_val <= curr.next.val:
            break
        # insert in the link position
        if curr.val > curr.next.val and (curr.val <= insert_val or insert_val <= curr.next.val):
            break
        curr = curr.next

        # insert new nodes
        insert_node = Node(insert_val, next=curr.next)
        curr.next = insert_node

        return head


def main():
    head = Node(3, Node(4))
    head.next.next = Node(1)
    head.next.next.next = head

    result = insert(head, 2)
    print('Result: ', result.val, result.next.val, result.next.next.val, result.next.next.next.val)


if __name__ == "__main__":
    main()