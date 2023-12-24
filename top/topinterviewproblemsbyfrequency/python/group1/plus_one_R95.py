"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
the integer. The digits are ordered from most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Tag: R95/145
Tag: 132/150
Tag: 66/2927, R361/2936 (overall frequency ranking)
"""


def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[0] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits


def plus_one_1(digits: list[int]) -> list[int]:
    # List -> Number
    n = 0
    for elem in digits:
        n = (n * 10) + elem
    n = n + 1

    # Number -> List
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n //= 10
    return digits


def main():
    digits = [1, 2, 3]
    print(plus_one(digits))


if __name__ == "__main__":
    main()
