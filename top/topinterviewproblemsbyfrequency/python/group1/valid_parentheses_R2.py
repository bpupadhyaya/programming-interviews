"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()[]{}"
Output: true

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

Tag: 52/150, R2/145 (top interview frequency ranking)
Tag: 20/2927, R2/2936 (overall frequency ranking)
"""


def is_valid(s: str) -> bool:
    # Create a pair of opening and closing parentheses.
    opcl = dict(('()', '[]', '{}'))
    # Create stack data structure.
    stack = []
    # Traverse each character in the input string.
    for idx in s:
        # If open parenthesis then append it to stack.
        if idx in '({[':
            stack.append(idx)
        # If the character is closing parenthesis, check that the same type opening parenthesis was pushed or not
        # If not, it is a mismatch and hence invalid
        elif len(stack) == 0 or idx != opcl[stack.pop()]:
            return False
    # At last, check if stack is empty or not. Empty means every open parenthesis was closed by a matching one.
    # Nonempty means mismatch
    return len(stack) == 0


def main():
    s = "()[]{}"
    print(is_valid(s))


if __name__ == "__main__":
    main()
