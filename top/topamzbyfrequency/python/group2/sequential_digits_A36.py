"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Tag: 1291/2927 , R980/2935 , R36/50 (amz)
"""
from collections import deque


def sequential_digits(low: int, high: int) -> list[int]:
    s = '123456789'
    ans = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            st = int(s[i:j+1])
            if low <= st <= high:
                ans.append(st)
    ans.sort()
    return ans


def sequential_digits_bfs(low: int, high: int) -> list[int]:
    queue = deque(range(1, 10))
    res = []
    while queue:
        u = queue.popleft()
        if low <= u <= high:
            res.append(u)
        elif high < u:
            continue

        last_num = u % 10
        if last_num != 9:
            queue.append(u * 10 + last_num + 1)

    return res


def main():
    low = 100
    high = 300
    print(sequential_digits_bfs(low, high))


if __name__ == "__main__":
    main()
