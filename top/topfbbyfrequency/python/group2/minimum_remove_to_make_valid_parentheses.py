"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Tag: fb R10/50, 1249/2927, R136/2936
"""

def minRemoveToMakeValid(s: str) -> str:
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)

def main():
    s = "a)b(c)d"
    print('Given: ', s, '\nAfter: ', minRemoveToMakeValid(s))

if __name__ == "__main__":
    main()