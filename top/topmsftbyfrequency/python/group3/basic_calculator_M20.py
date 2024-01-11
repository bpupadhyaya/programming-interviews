"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return
the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Example:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Tag: 56/150
Tag: 224/2927, R252/2936 (overall frequency ranking), M20/50
"""


def calculate(s: str) -> int:
    num = 0
    sign = 1
    res = 0
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '-+':
            res += num * sign
            sign = -1 if c == '-' else 1
            num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num * sign


def main():
    s = "(1+(4+5+2)-3)+(6+8)"
    print(calculate(s))


if __name__ == "__main__":
    main()
