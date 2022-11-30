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
        hashKey = key % self.keySpace
        self.hashTable[hashKey].update(key, value)

    def get(self, key):
        hashKey = key % self.keySpace
        return self.hashTable[hashKey].get(key)

    def remove(self, key):
        hashKey = key % self.keySpace
        self.hashTable[hashKey].remove(key)

def main():
    hashMap = MyHashMap()
    hashMap.put(5, 5)
    hashMap.put(10, 10)
    print(hashMap.get(5))
    print('\n')
    print(hashMap.get(15))
    hashMap.put(10, 5)
    print(hashMap.get(10))
    print('\n')
    hashMap.remove(10)
    print(hashMap.get(10))

if __name__ == "__main__":
    main()


