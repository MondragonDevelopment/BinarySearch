"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
"""

def shiftedBinarySearch(array, target):
    l, r = 0, len(array) - 1
    while l < r:
        m = (l + r) // 2
        if array[l] <= array[m]:
            if array[m] > target and array[l] <= target:
                temp = binarySearch(array[l: m], target)
                return -1 if temp == -1 else temp + l
            else: l = m+1
        else:
            if array[r] >= target and array[m] <= target:
                temp = binarySearch(array[m:r+1], target)
                return -1 if temp == -1 else temp + m
            else: r = m - 1
    return -1

def binarySearch(array, target):
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] < target:
            l = m + 1
        elif array[m] > target:
            r = m - 1
        else: return m
    return -1

# second method (simpler and more effective)
def search(array, target):
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if target == array[m]: return m
        if array[l] <= array[m]:
            if array[l] > target or array[m] < target:
                l = m + 1
            else: r = m - 1
        else:
            if array[m] > target or array[r] < target:
                r = m - 1
            else: l = m + 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
#nums = [5, 1, 3]
#target = 3
print(shiftedBinarySearch(nums, target))
print(search(nums, target))
