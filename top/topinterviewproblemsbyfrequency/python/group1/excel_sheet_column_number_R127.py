"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example:
Input: columnTitle = "AB"
Output: 28

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

R127/145
"""
from functools import reduce


def title_to_number(column_title: str) -> int:
    ans, pos = 0, 0
    for letter in reversed(column_title):
        digit = ord(letter) - 64
        ans += digit * 26**pos
        pos += 1
    return ans


def title_to_number_1(column_title: str) -> int:
    return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x)-ord('A')+1, column_title))


def title_to_number_2(column_title: str) -> int:
    ans = 0
    for i in column_title:
        ans = ans * 26 + ord(i) - ord('A') + 1
    return ans


def main():
    column_title = "AB"
    print(title_to_number(column_title))


if __name__ == "__main__":
    main()

"""
Explanation for title_to_number:
Essentially, what we asked to do here is to convert a number in the base 26 numeral system to a decimal number. 
This is a standard algorithm, where we iterate over the digits from right to left and multiply them by the base 
to the power of the position of the digit. To translate a letter to a number we use the Python method ord which 
returns the Unicode code of the letter. By subtracting the code by 64, we can map letters to the numbers from 1 to 26.
"""


