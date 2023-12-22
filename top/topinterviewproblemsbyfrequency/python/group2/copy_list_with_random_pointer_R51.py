"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node
has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the original list and copied list represent
the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair
of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does
not point to any node.
Your code will only be given the head of the original linked list.

Example:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Note: Visualize to understand

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.

Tag: Tag: R51/145
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    # Hashmap approach
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


def copy_random_list_1(head: Node) -> Node:
    # Interweaving nodes
    if not head:
        return None

    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    old_head = head
    new_head = head.next
    curr_old = old_head
    curr_new = new_head

    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next if curr_new.next else None
        curr_old = curr_old.next
        curr_new = curr_new.next

    return new_head


def main():
    head = Node(7, Node(13))
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    res = copy_random_list_1(head)
    print(head.val, head.next.val, head.next.random.val, head.next.next.val, head.next.next.random.val)
    print(head.next.next.next.val, head.next.next.next.random.val)
    print(head.next.next.next.next.val, head.next.next.next.next.random.val)


if __name__ == "__main__":
    main()

"""
Hash Map Method:
Intuition and Logic Behind the Solution
The basic idea is to traverse the list twice. In the first pass, we create a new node for each node in the original 
list and store the mapping in a hash map. In the second pass, we set the next and random pointers for each new node 
based on the hash map.

Step-by-step Explanation
Initialization:

Create an empty hash map, old_to_new, to store the mapping from old nodes to new nodes.
First Pass - Node Creation:

Traverse the original list and for each node, create a corresponding new node.
Store the mapping in old_to_new.
Second Pass - Setting Pointers:

Traverse the original list again.
For each node, set its corresponding new node's next and random pointers based on the hash map.
Complexity Analysis
Time Complexity: O(n)— Each node is visited twice.
Space Complexity: O(n) — To store the hash map.


Interweaving Nodes Method:
Intuition and Logic Behind the Solution
The crux of this method is to interweave the nodes of the original and copied lists. This interweaving allows us 
to set the random pointers for the new nodes without needing additional memory for mapping.

Step-by-step Explanation
Initialization and Interweaving:

Traverse the original list.
For each node, create a corresponding new node and place it between the current node and the current node's next.
Setting Random Pointers:

Traverse the interweaved list.
For each old node, set its corresponding new node's random pointer.
Separating Lists:

Traverse the interweaved list again to separate the old and new lists.
Complexity Analysis
Time Complexity: O(n) — Each node is visited multiple times but it's still linear time.
Space Complexity: O(1) — No additional memory is used for mapping; we only allocate nodes for the new list.
Both methods provide a deep copy of the original list but differ in their use of additional memory. The choice 
between them would depend on the specific requirements of your application.



"""

