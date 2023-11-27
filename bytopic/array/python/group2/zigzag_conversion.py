"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Tag: 22/150
Tag: 6/2927, R184/2936 (overall frequency ranking)
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s
    row_arr = [""] * num_rows
    row_idx = 1
    going_up = True
    for ch in s:
        row_arr[row_idx-1] += ch
        if row_idx == num_rows:
            going_up = False
        elif row_idx == 1:
            going_up = True
        if going_up:
            row_idx += 1
        else:
            row_idx -= 1
    return "".join(row_arr)


def main():
    s = "PAYPALISHIRING"
    num_rows = 4
    print(convert(s, num_rows))


if __name__ == "__main__":
    main()
