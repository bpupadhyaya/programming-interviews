"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Input: n = 1
Output: ["()"]

Tag: 106/150
Tag: 22/2927, R32/2936 (overall frequency ranking)
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
