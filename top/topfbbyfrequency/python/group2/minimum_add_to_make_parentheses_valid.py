"""
A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

- For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis
to be "())))".

Return the minimum number of moves required to make s valid.

Example:
    Input: s = "())"
    Output: 1

Tag: fb R24/50, 921/2927, R551/2936.
"""


def min_add_to_make_valid(s: str) -> int:
    opening = count = 0
    for i in s:
        if i == '(':
            opening += 1
        else:
            if opening:
                opening -= 1
            else:
                count += 1
    return count + opening


def min_add_to_make_valid_using_stack(s: str) -> int:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
    return len(stack)


def main():
    s = "())"
    print("Min moves: ", min_add_to_make_valid_using_stack(s))


if __name__ == "__main__":
    main()