import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

class Pair<K, V> {
    public K first;
    public V second;

    public Pair(K first, V second) {
        this.first = first;
        this.second = second;
    }
}

class Bucket {
    private List<Pair<Integer, Integer>> bucket;

    public Bucket() {
        this.bucket = new LinkedList<Pair<Integer, Integer>>();
    }

    public Integer get(Integer key) {
        for(Pair<Integer, Integer> pair: this.bucket) {
            if(pair.first.equals(key))
                return pair.second;
        }
        return -1;
    }

    public void update(Integer key, Integer value) {
        boolean found = false;
        for(Pair<Integer, Integer> pair: this.bucket) {
            if(pair.first.equals(key)) {
                pair.second = value;
                found = true;
            }
        }
        if (!found)
            this.bucket.add(new Pair<Integer, Integer>(key, value));
    }

    public void remove(Integer key) {
        for(Pair<Integer, Integer> pair: this.bucket) {
            if(pair.first.equals(key)) {
                this.bucket.remove(pair);
                break;
            }
        }
    }
}

class MyHashMap {
    private int keySpace;
    private List<Bucket> hashTable;

    public MyHashMap() {
        this.keySpace = 2069;
        this.hashTable = new ArrayList<Bucket>();
        for(int i = 0; i < this.keySpace; i++) {
            this.hashTable.add(new Bucket());
        }
    }

    public void put(int key, int value) {
        int hashKey = key % this.keySpace;
        this.hashTable.get(hashKey).update(key, value);
    }

    public int get(int key) {
        int hashKey = key % this.keySpace;
        return this.hashTable.get(hashKey).get(key);
    }

    public void remove(int key) {
        int hashKey = key % this.keySpace;
        this.hashTable.get(hashKey).remove(key);
    }
}

class MyHashMapApp {
    public static void main(String...args) {
        MyHashMap hashMap = new MyHashMap();
        hashMap.put(5,5);
        hashMap.put(10,10);
        System.out.println(hashMap.get(5));
        System.out.println(hashMap.get(15));
        hashMap.put(10,5);
        System.out.println(hashMap.get(10));
        hashMap.remove(10);
        System.out.println(hashMap.get(10));
    }
}