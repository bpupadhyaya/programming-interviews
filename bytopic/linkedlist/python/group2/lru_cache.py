"""
Design a data structure that follows the constraints of a LRU:
https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU
Implement the LRUCache class:
LRUCache(int capacity): initizlizes the LRU cache with positive size capacity.
int get(int key): return the value of the key if the key exists, otherwise return -1.
void put(int key, int value): update the value of the key if the key exists. Otherwise, add the key-value
pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently
used key.
The function get and put must each run on O(1) average time complexity.

Sample 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4
Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

Tag: 67/150
Tag: 146/2927, R12/2936 (overall frequency ranking), R7/100 (liked), R1/50 (amzn),  R9/145 (top interview)
R3/50 (msft)
"""
from collections import OrderedDict
from typing import Dict


class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data: Dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)


def main():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)             # cache is {1=1}
    lru_cache.put(2, 2)             # cache is {1=1, 2=2}
    print(lru_cache.get(1))         # return 1
    lru_cache.put(3, 3)             # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lru_cache.get(2))         # returns -1 (not found)
    lru_cache.put(4, 4)             # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lru_cache.get(1))         # return -1 (not found)
    print(lru_cache.get(3))         # return 3
    print(lru_cache.get(4))         # return 4


if __name__ == "__main__":
    main()

