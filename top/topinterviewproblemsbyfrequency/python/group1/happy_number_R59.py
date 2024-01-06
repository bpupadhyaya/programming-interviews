"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Tag: R59/145
"""


def is_happy(n: int) -> bool:
    hset = set()
    while n != 1:
        if n in hset:
            return False
        hset.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    else:
        return True


def main():
    n = 19
    print(is_happy(n))


if __name__ == "__main__":
    main()