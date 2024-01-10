"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing
one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and
 the ending string end, return True if and only if there exists a sequence of moves to transform one string to
  the other.

Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:
Input: start = "X", end = "L"
Output: false

Constraints:
1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.

Tag: G27/50
"""


def can_transform(start: str, end: str) -> bool:
    i, j = 0, 0
    n, m = len(start), len(end)

    while i < n and j < m:

        while i < n and start[i] == 'X':
            i += 1
        while j < m and end[j] == 'X':
            j += 1

        if (i == n) != (j == m):
            return False

        if i == n and j == m:
            return True

        if start[i] != end[j]:
            return False

        if start[i] == 'R' and i > j:
            return False
        if start[i] == 'L' and i < j:
            return False

        i += 1
        j += 1

    while i < n and start[i] == 'X':
        i += 1
    while j < m and end[j] == 'X':
        j += 1

    return i == n and j == m


def main():
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print(can_transform(start, end))


if __name__ == "__main__":
    main()
