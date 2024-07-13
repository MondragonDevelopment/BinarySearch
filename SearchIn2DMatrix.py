"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][-1] < target: continue
        l , r = 0, len(matrix[i]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[i][m] == target: return True
            elif matrix[i][m] < target:
                l = m + 1
            elif matrix[i][m] > target:
                r = m -1
        return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 23
print(searchMatrix(matrix, target))