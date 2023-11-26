"""
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least
one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Tag: 12/150
Tag: 380/2927, R137/2936 (overall frequency ranking)
"""
import random


class RandomizedSet:
    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)

    def remove(self, val: int) -> bool:
        if not (val in self.data_map):
            return False
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list
        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)

    def get_random(self) -> int:
        return random.choice(self.data)


def main():
    randomized_set = RandomizedSet()
    print(randomized_set.insert(1))     # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomized_set.remove(2))     # Returns false as 2 does not exist in the set.
    print(randomized_set.insert(2))     # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomized_set.get_random())  # getRandom() should return either 1 or 2 randomly.
    print(randomized_set.remove(1))     # Removes 1 from the set, returns true. Set now contains [2].
    print(randomized_set.insert(2))     # 2 was already in the set, so return false.
    print(randomized_set.get_random())  # Since 2 is the only number in the set, getRandom() will always return 2.


if __name__ == "__main__":
    main()
