#Two Pointers Solution
def sortedSquares(nums):
    L = 0
    R = len(nums) - 1
    out = []
    while L <= R:
        if (nums[L] ** 2) > (nums[R] ** 2):
            out.append(nums[L] ** 2)
            L += 1
        else:
            out.append(nums[R] ** 2)
            R -= 1
    out.reverse()
    return out

print(sortedSquares([-4, -1, 0, 3, 10]))

#sorting solution, faster
def sorted_squares(nums):
    out = []
    for num in nums:
        out.append(num ** 2)
    out.sort()
    return out

print(sorted_squares([-4, -1, 0, 3, 10]))