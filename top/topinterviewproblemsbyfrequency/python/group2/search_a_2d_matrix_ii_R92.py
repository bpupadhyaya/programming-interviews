"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix 'matrix'. This matrix has
the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9

R92/145
"""


def search_matrix_0(matrix: list[list[int]], target: int) -> bool:
    # O(m + n)
    m = len(matrix)
    n = len(matrix[0])

    i = m-1
    j = 0

    while i >= 0 and j<n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1

    return False


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # Complexity: O(m log n)
    # For each row -> O(m), binary search -> O(log n)
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][-1]:
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

    return False


def main():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(search_matrix_0(matrix, target))


if __name__ == "__main__":
    main()
