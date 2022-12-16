// Implement LRU Cache: initialization, value returning, and updating
// Time complexity: O(1), space complexity: Order(capacity)

import java.util.Map;
import java.util.LinkedHashMap;

class LRUCache extends LinkedHashMap<Integer,Integer> {
    private int capacity;

    LRUCache(int capacity) {
        super(capacity, 0.75F, true);
        this.capacity = capacity;
    }

    public int get(int key) {
        return super.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer,Integer> eldest) {
        return size() > capacity;
    }

    public static void main(String...args) {
        LRUCache lruCache = new LRUCache(5);
        lruCache.put(10, 10);
        lruCache.put(20, 20);
        System.out.println(lruCache.get(10));
        lruCache.put(30, 30);
        System.out.println(lruCache.get(20));
        lruCache.put(40, 40);
        System.out.println(lruCache.get(10));
        System.out.println(lruCache.get(30));
        System.out.println(lruCache.get(40));
    }

}
