#============================================================
# Custom HashSet
#============================================================
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

#============================================================
# Built In HashSet
#============================================================
# create
s = set()
s = {1, 2, 3}          # literal syntax
s = set([1, 2, 2, 3])  # from a list, dupes auto-removed -> {1, 2, 3}

# add / remove
s.add(4)
s.remove(2)      # raises KeyError if not present
s.discard(2)     # no error if not present
s.pop()           # removes and returns an arbitrary element

# check membership — O(1) average, same as your custom version
if 3 in s:
    print("found it")

# size
len(s)

# iterate
for item in s:
    print(item)

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)  # union -> {1, 2, 3, 4}
print(a & b)  # intersection -> {2, 3}
print(a - b)  # difference -> {1}
print(a ^ b)  # symmetric difference -> {1, 4}

a.issubset(b)  # False
a.issuperset(b)  # False
a.isdisjoint(b)  # False (they share elements)