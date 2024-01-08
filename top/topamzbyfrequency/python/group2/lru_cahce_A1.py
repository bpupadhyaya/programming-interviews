"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value
pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Tag: 146/2927 , R12/2935 , R1/50 (amz)
"""


class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def add_node(self, new_node):
        temp = self.head.next
        new_node.next = temp
        new_node.prev = self.head
        self.head.next = new_node
        temp.prev = new_node

    def delete_node(self, del_node):
        prevv = del_node.prev
        nextt = del_node.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.m:
            res_node = self.m[key]
            ans = res_node.val
            del self.m[key]
            self.delete_node(res_node)
            self.add_node(res_node)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.delete_node(curr)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.delete_node(self.tail.prev)

        self.add_node(self.Node(key, value))
        self.m[key] = self.head.next


def main():
    capacity = 2
    obj = LRUCache(capacity)
    obj.put(1, 1)                # cache is {1=1}
    obj.put(2, 2)                # cache is {1=1, 2=2}
    print(obj.get(1))           # return 1
    obj.put(3, 3)                # LRU key is 2, evicts key 2, cache is {1=1, 3=3}
    print(obj.get(2))           # returns -1, not found
    obj.put(4, 4)                # LRU key is 1, evicts key 1, cache is {4=4, 3=3}
    print(obj.get(1))           # returns -1, not found
    print(obj.get(3))           # returns 3
    print(obj.get(4))           # returns 4


if __name__ == "__main__":
    main()

"""
Intuition:
The intuition is to maintain a fixed-size cache of key-value pairs using a doubly linked list and an unordered map. 
When accessing or adding a key-value pair, it moves the corresponding node to the front of the linked list, making 
it the most recently used item. This way, the least recently used item is always at the end of the list. When the 
cache is full and a new item is added, it removes the item at the end of the list (least recently used) to make 
space for the new item, ensuring the LRU property is maintained.

Explanation:
1. Node Class:
- This is a nested class representing a doubly linked list node.
- Each node contains an integer key, an integer value, and pointers to the previous and next nodes in the linked list.

2. LRUCache Class:
- This is the main LRU Cache class.
- It has a fixed capacity (cap) that is specified during its instantiation.
- It uses an unordered_map<int, Node*> named m to store key-value pairs, where the key is the integer key, and the 
  value is a pointer to the corresponding Node.

3. head and tail Nodes:
- The LRUCache class has two dummy nodes: head and tail.
- These nodes act as sentinels in the doubly linked list, helping to simplify the edge cases and avoid dealing with 
  null pointers.
- head is the first node in the linked list, and tail is the last node.

4. addNode Function:
- This function is used to add a new node to the front of the doubly linked list (right after head).
- It takes a Node* newnode as input, representing the node to be added.
- The function updates the pointers of the new node, the previous first node, and head to include the new node as the 
  new first node.

5. deleteNode Function:
- This function is used to delete a node from the doubly linked list.
- It takes a Node* delnode as input, representing the node to be deleted.
- The function updates the pointers of the previous and next nodes to exclude the node to be deleted, effectively 
  removing it from the linked list.

6. get Function:
- This function is used to retrieve a value from the cache based on the given key.
- If the key exists in the cache (m.find(key) != m.end()), it retrieves the corresponding node (resNode), extracts 
  its value (ans), and performs the following steps:
 -- Erase the key-value pair from the m unordered map.
 -- Delete the node from its current position in the linked list using deleteNode.
 -- Add the node to the front of the linked list using addNode, making it the most recently used node.
 -- Update the m map to store the key with the most recently used node.
   If the key doesn't exist in the cache, it returns -1.

7. put Function:
- This function is used to insert or update a key-value pair in the cache.
- If the key already exists in the cache, it updates the value by performing the following steps:
 -- Erase the existing key-value pair from the m unordered map.
 -- Delete the corresponding node from its current position in the linked list using deleteNode.
- If the cache is full (i.e., m.size() == cap), it removes the least recently used node from the cache by erasing 
  the key-value pair from the m map and deleting the node from the end of the linked list using deleteNode.
- After handling the eviction (if needed), it creates a new node using new Node(key, value) and adds it to the front 
  of the linked list using addNode.
- Finally, it updates the m map to store the key with the newly added node.
"""