"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()[]{}"
Output: true
Example 2:
Input: s = "(]"
Output: false

Tag: 52/150
Tag: 20/2927, R2/2936 (overall frequency ranking)
"""


def is_valid(s: str) -> bool:
    # Create a pair of opening and closing parentheses.
    open_close = dict(('()', '[]', '{}'))
    # create stack data structure
    stack = []
    # Traverse each character in input string
    for idx in s:
        # If open parenthesis is present, append it to stack
        if idx in '([{':
            stack.append(idx)
        # If the character is closing parenthesis, check that the same type of opening is being pushed to the stack
        # or not. If not, we return false to indicate invalid parentheses combination.
        elif len(stack) == 0 or idx != open_close[stack.pop()]:
            return False
    # At last, we check if the stack is empty. Empty stack means there was open-close parentheses match. Non-empty
    # stack means mismatch
    return len(stack) == 0


def main():
    s = "()[]{}"
    print(is_valid(s))


if __name__ == "__main__":
    main()
