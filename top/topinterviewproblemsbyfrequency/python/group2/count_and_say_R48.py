"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted
into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring
contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit.
Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
"3322251"
two 3's, three 2's, one 5, and one 1
23+32+15+11
"23321511"

Given a positive integer n, return the nth term of the count-and-say sequence.

Example:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
1 <= n <= 30


Tag: R48/145
"""
from itertools import groupby


def count_and_say(n: int) -> str:
    if n == 1:
        return "1"
    x = count_and_say(n-1)
    s = ""
    y = x[0]
    ct = 1
    for i in range(1, len(x)):
        if x[i] == y:
            ct += 1
        else:
            s += str(ct)
            s += str(y)
            y = x[i]
            ct = 1
    s += str(ct)
    s += str(y)
    return s


def count_and_say_1(n: int) -> str:
    # Recursive
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))

    if n == 1:
        return '1'
    return make_count(count_and_say_1(n-1))


def count_and_say_2(n: int) -> str:
    # Iterative
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))

    string = '1'
    for _ in range(n-1):
        string = make_count(string)
    return string


def main():
    n = 4
    print(count_and_say_2(n))


if __name__ == "__main__":
    main()
