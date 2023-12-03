"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Sample 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Tag: 115/150
Tag: 74/2927, R236/2936 (overall frequency ranking)
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_row, mid_col = divmod(mid, n)

        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 13
    print(search_matrix(matrix, target))


if __name__ == "__main__":
    main()
