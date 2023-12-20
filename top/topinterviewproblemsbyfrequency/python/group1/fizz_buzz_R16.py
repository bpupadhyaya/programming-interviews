"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:
Input: n = 3
Output: ["1","2","Fizz"]

Constraints:
1 <= n <= 10^4

Tag: R16/145
"""


def fizz_buzz(n: int) -> list[str]:
    f, b, fb, = 'Fizz', 'Buzz', 'FizzBuzz'
    arr = [str(x + 1) for x in range(n)]
    for i in range(2, n, 3):
        arr[i] = f
    for i in range(4, n, 5):
        arr[i] = b
    for i in range(14, n, 15):
        arr[i] = fb
    return arr


def main():
    n = 3
    print(fizz_buzz(n))


if __name__ == "__main__":
    main()
