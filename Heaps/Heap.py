#Example of min heap class:
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def push(self, val):
        self.heap.append(val)          # add at the end
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            parent = self._parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        top = self.heap[0]
        last = self.heap.pop()         # remove last element
        if self.heap:                  # if anything left, move last to root
            self.heap[0] = last
            self._sift_down(0)
        return top

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def peek(self):
        return self.heap[0] if self.heap else None

# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
import heapq
heapq.heapify(A)
print(A)

#Heap Push, inserting element
# O(logN)
heapq.heappush(A, 4)
print(A)

#Heap pop, extract Min val
# Time: O(log n)
minn = heapq.heappop(A)
print(A, minn)

#Heap sort, O(n log n), space: O(n)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_arr = [0] * n
    for i in range(n):
        minimum = heapq.heappop(arr)
        new_arr[i] = minimum
    return new_arr


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

#Heap push pop, time: O(log n)
heapq.heappushpop(A, 99)
print(A)

#Peek at min: O(1)
print(A[0])


#Max Heap
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print(B)

largest = -heapq.heappop(B)
print(largest)

heapq.heappush(B, -7) # inserts pos 7 into max heap

# Build heap from scratch, time: O(n log n), slower than calling heapify
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap))


#Tuples of items on the heap:
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
from collections import Counter
counter = Counter(D)
print(counter)


heap = []
# smallest frequency on top, and if ties it will compare by key
for k, v, in counter.items():
    heapq.heappush(heap, (v,k))

print(heap)