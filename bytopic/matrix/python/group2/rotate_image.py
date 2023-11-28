"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Note: visualize to understand

Tag: 36/150
Tag: 48/2927, R38/2936 (overall frequency ranking)
"""


def rotate(matrix: list[list[int]]) -> None:
    # reverse
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1
    # transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()
