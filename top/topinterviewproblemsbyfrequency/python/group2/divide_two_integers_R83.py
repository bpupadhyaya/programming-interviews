"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would
be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−2^{31}, 2^{31} − 1]. For this problem, if the quotient is strictly greater than 2^{31} - 1, then return
2^{31} - 1, and if the quotient is strictly less than -2^{31}, then return -2^{31}.

Example:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-2^{31} <= dividend, divisor <= 2^{31} - 1
divisor != 0

R83/145
"""


def divide(dividend: int, divisor: int) -> int:
    sign = -1 if (dividend >= 0 > divisor) or (dividend < 0 <= divisor) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = len(range(0, dividend - divisor + 1, divisor))
    if sign == -1:
        result = -result
    minus_limit = -(2**31)
    plus_limit = (2**31-1)
    result = min(max(result, minus_limit), plus_limit)
    return result


def main():
    dividend = 7
    divisor = -3
    print(divide(dividend, divisor))


if __name__ == "__main__":
    main()

"""
Steps for divide:
Define the result's sign and operate with positive dividend and divisor.
Calculate the result using the length of range.
Apply the sign.
Apply the 32-bit integer limitations.


"""
