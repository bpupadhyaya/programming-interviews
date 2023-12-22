"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Tag: R46/145
"""


def my_pow_simple(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    result = my_pow_simple(x, n // 2)
    if n % 2 == 0:
        return result * result
    else:
        return x * result * result


def my_pow(x: float, n: int) -> float:
    def func(base=x, exponent=abs(n)):
        if exponent == 0:
            return 1
        # Note: there is formula in mathematics for odd and even n, search in internet
        elif exponent % 2 == 0:
            return func(base * base, exponent // 2)
        else:
            return base * func(base * base, (exponent - 1) // 2)
    f = func()
    return float(f) if n >= 0 else 1/f


def main():
    x = 2.00000
    n = 10
    print(my_pow_simple(x, n))


if __name__ == "__main__":
    main()


"""
Explanation for simple approach:
Base case: n is zero, x^0 is 1
If n is negative, convert x to its reciprocal and change n to positive
If n is even, use the formula (x^n/2)^2. Otherwise x * (x^((n-1)/2))^2 (note: check the validity of this formula)
Complexity
Time complexity: O(n) to O(log n) depending the input case
Space complexity: O(log n) extra space for each callstack. (recursive binary tree)

"""