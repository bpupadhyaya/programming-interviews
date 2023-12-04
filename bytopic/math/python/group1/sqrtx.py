"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Tag: 134/150
Tag: 69/2927, R187/2936 (overall frequency ranking)
"""


def my_sqrt_using_normal_math(x: int) -> int:
    number = 1
    while number * number <= x:
        number += 1
    return number


def my_sqrt_using_binary_search(x: int) -> int:
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return right


def main():
    x = 8
    print(my_sqrt_using_binary_search(x))


if __name__ == "__main__":
    main()
