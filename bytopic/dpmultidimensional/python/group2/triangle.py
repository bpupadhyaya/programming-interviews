"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the
current row, you may move to either index i or index i + 1 on the next row.

Example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Tag: 142/150
Tag: 120/2927, R497/2936 (overall frequency ranking)
"""


def minimum_total(triangle: list[list[int]]) -> int:
    for i in range(1, len(triangle)):
        for j in range(i+1):
            triangle[i][j] += min(triangle[i-1][j-(j == i)], triangle[i-1][j-(j > 0)])
    return min(triangle[-1])


def main():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minimum_total(triangle))


if __name__ == "__main__":
    main()
