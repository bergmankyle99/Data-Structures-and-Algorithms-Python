#====================================================
# Traditional Binary Search
# Time O(log(n))
# space = O(1)
#====================================================
def binary_search(array, target):
    n = len(array)
    L = 0
    R = n - 1

    while L <= R:
        M = L + ((R-L) // 2)
        if array[M] == target:
            return True
        elif array[M] < target:
            R = M - 1
        else:
            L = M + 1
    return False

A = [-3, -1, 0, 1, 2, 3]
print(binary_search(A, -50))

#====================================================
# Over Under Binary Search
# based on a condition
#====================================================

B = [False,False,False,False,True,True,True,True,True,True]

def binary_search_condition(array):
    N = len(array)
    L = 0
    R = N - 1
    while L < R:
        M = L + ((R - L) // 2)
        if array[M]:
            R = M
        else:
            L = M + 1
    return L

print(binary_search_condition(B))