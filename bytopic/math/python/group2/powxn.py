"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Sample 1:
Input: x = 2.00000, n = -2
Output: 0.25000

Tag: 135/150
Tag: 50/2927, R98/2936 (overall frequency ranking), fb R5/50
"""
from functools import cache


def my_pow(x: float, n: int) -> float:
    # Search in google, there is math formula for x^n for n is odd and n is even
    def function(base=x, exponent=abs(n)):
        if exponent == 0:
            return 1
        elif exponent % 2 == 0:
            return function(base * base, exponent // 2)
        else:
            return base * function(base * base, (exponent - 1) // 2)
    f = function()

    return float(f) if n >= 0 else 1/f


@cache
def my_pow_using_divide_and_conquer(x: float, n: int) -> float:
    # Idea: x^2 = x^1 * x^1 * x^0
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1/x
    return my_pow_using_divide_and_conquer(x, n // 2) * my_pow_using_divide_and_conquer(x, n // 2) * \
        my_pow_using_divide_and_conquer(x, n % 2)


def main():
    x = 2.00000
    n = -2
    print(my_pow_using_divide_and_conquer(x, n))


if __name__ == "__main__":
    main()
