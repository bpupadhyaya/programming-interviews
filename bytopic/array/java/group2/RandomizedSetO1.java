// Implement the RandomizedSet class:
// - RandomizedSet() Initializes the RandomizedSet object.
// - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
// false otherwise.
// - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
// false otherwise.
// - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least
// one element exists when this method is called). Each element must have the same probability of being returned.
// You must implement the functions of the class such that each function works in average O(1) time complexity.
// Input
// ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
// [[], [1], [2], [2], [], [1], [2], []]
// Output
// [null, true, false, true, 2, true, false, 2]
//
// Tag: 12/150
// Tag: 380/2927, R137/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;
class RandomizedSet {
    ArrayList<Integer> nums;
    HashMap<Integer, Integer> locs;
    Random rand = new Random();

    public RandomizedSet() {
        nums = new ArrayList<Integer>();
        locs = new HashMap<Integer, Integer>();
    }

    public boolean insert(int val) {
        boolean contain = locs.containsKey(val);
        if (contain) return false;
        locs.put(val, nums.size());
        nums.add(val);
        return true;
    }

    public boolean remove(int val) {
        boolean contain = locs.containsKey(val);
        if (!contain) return false;
        int loc = locs.get(val);
        if (loc < nums.size() - 1) { // if not the last one then swap the last one ith this val
            int last = nums.get(nums.size() - 1);
            nums.set(loc, last);
            locs.put(last, loc);
        }
        locs.remove(val);
        nums.remove(nums.size() - 1);
        return true;
    }

    // GEt a random element from the set
    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }

}
class RandomizedSetO1 {
    public static void main(String[] args) {
        RandomizedSet randomizedSet = new RandomizedSet();
        System.out.println(randomizedSet.insert(1)); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
        System.out.println(randomizedSet.remove(2)); // Returns false as 2 does not exist in the set.
        System.out.println(randomizedSet.insert(2)); // Inserts 2 to the set, returns true. Set now contains [1,2].
        System.out.println(randomizedSet.getRandom()); // getRandom() should return either 1 or 2 randomly.
        System.out.println(randomizedSet.remove(1)); // Removes 1 from the set, returns true. Set now contains [2].
        System.out.println(randomizedSet.insert(2)); // 2 was already in the set, so return false.
        System.out.println(randomizedSet.getRandom()); // Since 2 is the only number in the set, getRandom() will always return 2.
    }
}

// Explanation
// RandomizedSet randomizedSet = new RandomizedSet();
// randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
// randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
// randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
// randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
// randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
// randomizedSet.insert(2); // 2 was already in the set, so return false.
// randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.