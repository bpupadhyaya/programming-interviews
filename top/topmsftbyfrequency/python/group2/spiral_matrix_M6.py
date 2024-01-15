"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Note: Visualize to understand

Tag: R17/145
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1
    col_end = len(matrix[0])-1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1
        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
            row_end -= 1
        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    return res


def spiral_order_1(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # Traverse down
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse left
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse up
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral_order_1(matrix))


if __name__ == "__main__":
    main()
