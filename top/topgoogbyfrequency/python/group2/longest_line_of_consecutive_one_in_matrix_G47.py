"""
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal, or anti-diagonal.

Example:
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3

Example:
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.

Tag: G47/50
"""


def longest_line(mat: list[list[int]]) -> int:
    m, n = len(mat), len(mat[0])

    # keep track of the largest size of consecutive 1s
    row_map, col_map = [0] * m, [0] * n
    fdi_map, bdi_map = [0] * (m + n), [0] * (m + n)
    row_max = col_max = fdi_max = bdi_max = 0

    for x in range(m):
        for y in range(n):
            if mat[x][y] == 0:
                # reset all the values associated to this location to 0
                row_map[x] = col_map[y] = fdi_map[x + y] = bdi_map[x - y] = 0
            else:
                # increment all the values associated to this location by 1
                row_map[x] += 1
                col_map[y] += 1
                fdi_map[x + y] += 1
                bdi_map[x - y] += 1
                row_max = max(row_max, row_map[x])
                col_max = max(col_max, col_map[y])
                fdi_max = max(fdi_max, fdi_map[x + y])
                bdi_max = max(bdi_max, bdi_map[x - y])

    # return the maximum among 4 different orientations
    return max(row_max, col_max, fdi_max, bdi_max)


def main():
    mat = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]
    print(longest_line(mat))


if __name__ == "__main__":
    main()
