"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Tag: R119/145
Tag: 55/150
Tag: 150/2927, R668/2936 (overall frequency ranking)
Note: Both implementations work for some input but not all, debug and fix.
"""
from math import trunc


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    for t in tokens:
        if t not in '/+-*':
            stack.append(int(t))
        else:
            num = stack.pop()
            if t == '+':
                stack[-1] += num
            if t == '-':
                stack[-1] -= num
            if t == '*':
                stack[-1] *= num
            else:
                stack[-1] = int(stack[-1] / num)
    return stack[0]


def eval_rpn_1(tokens: list[str]) -> int:
    stack_ = []
    for i in tokens:
        if i not in {"+", "-", "*", "/"}:
            stack_.append(int(i))
        else:
            b, a = stack_.pop(), stack_.pop()
            if i == "+":
                stack_.append(a + b)
            elif i == "-":
                stack_.append(a - b)
            elif i == "*":
                stack_.append(a*b)
            else:
                stack_.append(trunc(a/b))
    return stack_[0]


def main():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(eval_rpn(tokens))


if __name__ == "__main__":
    main()
