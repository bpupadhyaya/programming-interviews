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


def main():
    n = 3
    print(generate_parentheses(n))


if __name__ == "__main__":
    main()


"""
Idea:
The idea is to add ')' only after valid '('
We use two integer variables left & right to see how many '(' & ')' are in the current string
If left < n then we can add '(' to the current string
If right < left then we can add ')' to the current string
"""
