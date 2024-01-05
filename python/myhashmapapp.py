class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):
    def __init__(self):
        self.keySpace = 2069
        self.hashTable = [Bucket() for i in range(self.keySpace)]

    def put(self, key, value):
        hash_key = key % self.keySpace
        self.hashTable[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.keySpace
        return self.hashTable[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.keySpace
        self.hashTable[hash_key].remove(key)


def main():
    hash_map = MyHashMap()
    hash_map.put(5, 5)
    hash_map.put(10, 10)
    print(hash_map.get(5))
    print(hash_map.get(15))
    hash_map.put(10, 5)
    print(hash_map.get(10))
    hash_map.remove(10)
    print(hash_map.get(10))


if __name__ == "__main__":
    main()
