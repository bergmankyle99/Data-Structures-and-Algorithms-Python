# Bubble sort, time: O(n^2), space: O(1)
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(A)

#insertion sort, time: O(n^2), space: O(1)
B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

insertion_sort(B)
print(B)

C = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
#Selection Sort, time: O(n^2), space: O(1)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort(C)
print(C)


#merge sort, divide and conquer algorithm Time: O(n log n), space: O(n)
D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    m = n // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)

    sorted = [0] * n
    i = 0
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted[i] = L[l]
            l += 1
        else:
            sorted[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted[i] = R[r]
        r += 1
        i += 1

    return sorted

print(merge_sort(D))


E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
#Quick Sort, Time: good pivot = O(n log n), bad pivots = O(n^2), Space: O(n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    L = [x for x in arr[:-1] if x <= p] # every item in the array, up to the last element where x <= pivot
    R = [x for x in arr[:-1] if x > p]
    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

print(quick_sort(E))

F = [5, 3, 2, 1, 3, 3, 7, 2, 2] # can do counting sort with negative values but its annoying so only on positive values
def counting_sort(arr): # Time: O(k + n), Space: O(k) where k is the max in the array. If k is huge, bad algo. if k is small its close to linear
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)
    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1


counting_sort(F)
print(F)



#what we usually do in practice
# Timsort = O(n log n)
G = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
# in place, constant space
G.sort()
print(G)
#get new sorted array, O(n) space
H = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
sorted_h = sorted(H)
print(H, sorted_h)

#sort array of tuples
I = [(-5, 3),(2, 1),(-3, -3),(7, 2),(2, 2)] #leetcode problem intervals
sorted_I = sorted(I, key = lambda t: t[0]) # lambda basically says, for tuple t do the comparison on t[0] (first postion) or t[1] for second position. If want reverse order to -t[0] or -t[1]
print(sorted_I)

