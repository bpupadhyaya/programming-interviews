"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Note visualize grid for better understanding
Note: compiles but wrong output, debug and fix.

Tag: 107/150
Tag: 79/2927, R340/2936 (overall frequency ranking)
"""
from collections import Counter


def exist(board: list[list[str]], word: str) -> bool:
    rr = len(board)
    cc = len(board[0])
    if len(word) > rr * cc:
        return False
    count = Counter(sum(board, []))
    for c, count_word in Counter(word).items():
        if count[c] < count_word:
            return False
    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    seen = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rr or c >= cc or word[i] != board[r][c] or (r, c) in seen:
            return False
        seen.add((r, c))
        res = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
        )
        seen.remove((r, c))  # backtracking

        return res

    for i in range(rr):
        for j in range(cc):
            if dfs(i, j, 0):
                return True
    return False


def main():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(board, word)


if __name__ == "__main__":
    main()
