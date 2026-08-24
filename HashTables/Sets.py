#lookup
#add
#delete

class HashSet:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

    #hash
    def hash(self, key):
        return hash(key) % self.capacity

    #add
    def add(self, key):
        if self.contains(key):
            return
        idx = self.hash(key)
        self.buckets[idx].append(key)
        self.size += 1
        if self.size / self.capacity >= 0.7:
            self.resize()

    #lookup
    def lookup(self, key):
        if self.contains(key):
            return self.hash(key)
        else:
            return -1

    #delete
    def delete(self, key):
        if not self.contains(key):
            return
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if key in bucket:
            bucket.remove(key)
            self.size -= 1

    #resize
    def resize(self):
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(self.capacity * 2)]
        self.capacity *= 2
        self.size = 0
        for bucket in old_buckets:
            for key in bucket:
                self.add(key)

    #contains
    def contains(self, key):
        idx = self.hash(key)
        if key in self.buckets[idx]:
            return True
        else:
            return False



hashset = HashSet()
hashset.add("kyle")
hashset.add("Josh")
hashset.add("g")
print(hashset.buckets)
print(hashset.lookup("kyle"))
hashset.delete("kyle")
print(hashset.buckets)