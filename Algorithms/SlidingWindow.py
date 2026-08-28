#Variable Length Sliding Window
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    longest = 0
    sett = set()
    n = len(s)
    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        w = (r - l) + 1
        longest = max(w, longest)
        sett.add(s[r])

    return longest

print(lengthOfLongestSubstring("abcabcbb"))

#Fixed length sliding window
def findMaxAverage(nums, k: int) -> float:
    n = len(nums)
    curr_sum = 0
    for i in range(k):
        curr_sum += nums[i]

    max_avg = curr_sum / k
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]

        max_avg = max(max_avg, (curr_sum / k))

    return max_avg

print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))