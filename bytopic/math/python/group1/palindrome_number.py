"""
Given an integer, return true if the integer is a palindrome, and false if otherwise.

Sample 1:
Input 242
Output: true

Sample 2:
Input: -242
Output: false, explanation: from lef it reads -242, from right it reads 242- and hence not a palindrome.

Tag: 131/150
Tag: 9/2927, R11/2936 (overall frequency ranking)
"""


def is_palindrome_for_beginner(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


def is_palindrome_for_beginner_numeric(x: int) -> bool:
    if x < 0:
        return False
    input_num = x
    new_num = 0
    while x > 0:
        new_num = new_num * 10 + x % 10
        x = x // 10
    return new_num == input_num


def is_palindrome_faster(x: int) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0):  # if x is negative, return False. if x is positive and last digit is 0,
        # that also cannot form a palindrome, return False.
        return False
    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10
    return True if (x == result or x == result // 10) else False


def main():
    x = 242
    print(is_palindrome_faster(x))


if __name__ == "__main__":
    main()
