"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example:
Input: n = 27
Output: true
Explanation: 27 = 33

Constraints:
-2^{31} <= n <= 2^{31} - 1

Follow up: Could you solve it without loops/recursion?

R143/145
"""
import math


def is_power_of_three(n: int) -> bool:
    return n > 0 and 3 ** 19 % n == 0


def is_power_of_three_1(n: int) -> bool:
    if n <= 0:
        return False
    log = math.log10(n) / math.log10(3)
    return int(log) == log


def main():
    n = 27
    print(is_power_of_three_1(n))


if __name__ == "__main__":
    main()

"""
Explanation for is_power_of_three:
Note: validate the logic (todo)
Approach
The condition n > 0 is used to make sure that we only check for positive integers.
We check if 3 raised to the power of 19 is divisible by n. Why 19? Because 3**19 is the largest power of 3 that can 
fit into the integer range (2^31 - 1).
If n is a power of 3, then it must be a divisor of 319 and thus the remainder of 319 / n will be 0. If it's not a 
power of 3, then it won't be a divisor and the remainder will be non-zero.
Therefore, we return True if n is greater than 0 and 3**19 % n is equal to 0, and False otherwise.

Explanation for is_power_of_three_1:
Intuition
To check if an integer n is a power of three, we can use the logarithm function to solve it. Specifically, we can 
take the logarithm of n with base 3 and check if the result is an integer. If the result is an integer, then n is 
a power of three. Otherwise, n is not a power of three.

Approach
The approach is to use the built-in logarithm function in Python to implement this solution. We first check if n 
is non-positive, in which case it cannot be a power of three. Then, we take the logarithm of n with base 3 using 
the math.log10() function. We divide by the logarithm of 3 to convert the result to base 3. Finally, we check if
 the result is an integer using the int() function and compare it to the original result. If they are equal, then
  n is a power of three.

Complexity
Time complexity: O(1)
Space complexity: O(1)
The time complexity is O(1) since we are just taking logarithms and performing basic arithmetic operations.
 The space complexity is also O(1) since we are not using any additional space apart from the input variable
  and a few variables to store intermediate results.

"""
