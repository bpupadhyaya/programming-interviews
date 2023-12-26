"""
There is a singly-linked list head and we want to delete a node node in it.
You are given the node to be deleted node. You will not be given access to the first node of head.
All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in
the linked list.
Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:
For the input, you should provide the entire linked list head and the node to be given node. node should not be
the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

Example:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after
calling your function.

R109/145
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next


def main():
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    delete_node(head.next)
    print(head.val, head.next.val, head.next.next.val)


if __name__ == "__main__":
    main()

"""
Approach:
We delete the node by "replacing" the node with node.next.
node.val change to node.next.val
node.next change to node.next.next

Time complexity: O(1)
The algorithm only needs two assignment operations.
Space complexity: O(1)
The algorithm doesn't need extra memory.
"""