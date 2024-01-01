"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Tag: Tag: R22/145
"""


def generate_parentheses(n: int) -> list[str]:
    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return
        if left < n:
            dfs(left+1, right, s+'(')
        if right < left:
            dfs(left, right+1, s+')')
    res = []
    dfs(0, 0, '')
    return res


def generate_parentheses_1(n: int) -> list[str]:
    ans=[]

    def back_tracking(curr, open_brackets, close_brackets):
        # Base case
        if open_brackets == close_brackets == n:
            ans.append("".join(curr))
            return

        # close_brackets is less than open_brackets
        if close_brackets < open_brackets:
            curr.append(")")
            back_tracking(curr, open_brackets, close_brackets + 1)
            curr.pop()

        # open_brackets is less than the input
        if open_brackets < n:
            curr.append("(")
            back_tracking(curr, open_brackets + 1, close_brackets)
            curr.pop()

    back_tracking(["("], 1, 0)

    return ans


def main():
    n = 3
    print(generate_parentheses_1(n))


if __name__ == "__main__":
    main()


"""
Idea:
The idea is to add ')' only after valid '('
We use two integer variables left & right to see how many '(' & ')' are in the current string
If left < n then we can add '(' to the current string
If right < left then we can add ')' to the current string

generate_parentheses_1 explanation:
Intuition
We can just start thinking on this problem by drawing decision try and by observing the tree you may figure it out 
that this is a Back-Tracking challenge!

Approach
Just we will start by adding an opening bracket. To have balanced parenthesis we need to have equal number of 
opening and closing brackets.
Two things to remember:

We can add an opening bracket when the number of opening brackets is less than n.
We can add closing bracket only when count of open brackets is more than closing brackets.
"""
