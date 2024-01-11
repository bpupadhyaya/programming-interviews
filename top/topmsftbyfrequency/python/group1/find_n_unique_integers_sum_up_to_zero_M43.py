"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]

Constraints:
1 <= n <= 1000

Tag: M43/50
"""


def sum_zero(n: int) -> list[int]:
    l, rem = n // 2, n % 2
    if rem != 0:
        ans = [0]
    else:
        ans = []
    for i in range(1, l+1):
        ans.append(-i)
        ans.append(i)
    return ans


def sum_zero_0(n: int) -> list[int]:
    return list(range(1, n))+[-n*(n-1)//2]


def sum_zero_1(n: int) -> list[int]:
    return list(range(-(n//2), 0)) + [0]*(n % 2) + list(range(1, n//2 + 1))


def main():
    n = 3
    print(sum_zero_1(n))


if __name__ == "__main__":
    main()
