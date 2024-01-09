"""
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the
range of [-2^{31}, 2^{31} - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^{31} - 1].
The answer is guaranteed to fit in a 32-bit integer.

R67/145, F12/50
"""
import math


def calculate(s: str) -> int:
    num = 0
    res = 0
    pre_op = '+'
    s += '+'
    stack = []
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == ' ':
            pass
        else:
            if pre_op == '+':
                stack.append(num)
            elif pre_op == '-':
                stack.append(-num)
            elif pre_op == '*':
                operand = stack.pop()
                stack.append((operand * num))
            elif pre_op == '/':
                operand = stack.pop()
                stack.append(math.trunc(operand / num))
            num = 0
            pre_op = c
    return sum(stack)


def main():
    s = " 3+5 / 2 "
    print(calculate(s))


if __name__ == "__main__":
    main()