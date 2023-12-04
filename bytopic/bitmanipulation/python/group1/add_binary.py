"""
Given two binary strings a and b, return their sum as a binary string.

Sample 1:
Input: a = "1010", b = "1011"
Output: "10101"

Tag: 125/150
Tag: 67/2927, R356/2936 (overall frequency ranking)
"""


def add_binary(a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2
    return ''.join(reversed(s))


def main():
    a = "1010"
    b = "1011"
    print(add_binary(a, b))


if __name__ == "__main__":
    main()
