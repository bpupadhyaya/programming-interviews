// Design a data structure that follows the constraints of a LRU:
// https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU
// Implement the LRUCache class:
// LRUCache(int capacity): initizlizes the LRU cache with positive size capacity.
// int get(int key): return the value of the key if the key exists, otherwise return -1.
// void put(int key, int value): update the value of the key if the key exists. Otherwise, add the key-value
// pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently
// used key.
// The function get and put must each run on O(1) average time complexity.
// Sample 1:
// Input:
// ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
// Output:
// [null, null, null, 1, null, -1, null, -1, 3, 4]
// Explanation
// LRUCache lRUCache = new LRUCache(2);
// lRUCache.put(1, 1); // cache is {1=1}
// lRUCache.put(2, 2); // cache is {1=1, 2=2}
// lRUCache.get(1);    // return 1
// lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
// lRUCache.get(2);    // returns -1 (not found)
// lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
// lRUCache.get(1);    // return -1 (not found)
// lRUCache.get(3);    // return 3
// lRUCache.get(4);    // return 4
// Constraints:
// 1 <= capacity <= 3000
// 0 <= key <= 10^4
// 0 <= value <= 10^5
// At most 2 * 10^5 calls will be made to get and put.
//
// Tag: 67/150
// Tag: 146/2927, R12/2936 (overall frequency ranking), R7/100 (liked), R1/50 (amzn),  R9/145 (top interview)
// R3/50 (msft)

import java.util.HashMap;
class LRUCache {
    class Node {
        int key;
        int val;
        Node prev;
        Node next;

        Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    Node head = new Node(-1, -1);
    Node tail = new Node(-1, -1);
    int cap;
    HashMap<Integer, Node> m = new HashMap<>();

    public LRUCache(int capacity) {
        cap = capacity;
        head.next = tail;
        tail.prev = head;
    }

    private void addNode(Node newNode) {
        Node temp = head.next;
        newNode.next = temp;
        newNode.prev = head;
        head.next = newNode;
        temp.prev = newNode;
    }

    private void deleteNode(Node delNode) {
        Node prevv = delNode.prev;
        Node nextt = delNode.next;
        prevv.next = nextt;
        nextt.prev = prevv;
    }

    public int get(int key) {
        if (m.containsKey(key)) {
            Node resNode = m.get(key);
            int ans = resNode.val;
            m.remove(key);
            deleteNode(resNode);
            addNode(resNode);
            m.put(key, head.next);
            return ans;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (m.containsKey(key)) {
            Node curr = m.get(key);
            m.remove(key);
            deleteNode(curr);
        }
        if (m.size() == cap) {
            m.remove(tail.prev.key);
            deleteNode(tail.prev);
        }

        addNode(new Node(key, value));
        m.put(key, head.next);
    }


    public static void main(String...args) {
        LRUCache lruCache = new LRUCache(2);
        lruCache.put(1,1);
        lruCache.put(2,2);
        System.out.println(lruCache.get(1));
        lruCache.put(3,3);
        System.out.println(lruCache.get(2));
        lruCache.put(4,4);
        System.out.println(lruCache.get(1));
        System.out.println(lruCache.get(3));
        System.out.println(lruCache.get(4));
    }
}