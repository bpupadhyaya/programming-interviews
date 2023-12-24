"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Note: Visualize to understand

Tag: R108/145
Tag: 100/150
Tag: 212/2927, R469/2936 (overall frequency ranking)
"""


class Trie:
    def __init__(self, words: list[str]=None):
        # The variable length stores the total number of children of this node.
        self.root = {"length": 0}
        for word in words:
            self.insert(word)

    def __len__(self) -> int:
        return self.root["length"]

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    def remove(self, word: str) -> None:
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    current.pop(c)
                    break
                else:
                    current = current[c]
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    def contains(self, word: list[str]) -> int:
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    num_rows, num_cols = len(board), len(board[0])
    seq_two = set()
    candidates = []
    reversed_words = set()
    for i in range(num_rows):
        for j in range(num_cols - 1):
            seq_two.add(board[i][j] + board[i][j+1])
    for j in range(num_cols):
        for i in range(num_rows - 1):
            seq_two.add(board[i][j] + board[i+1][j])
    for word in words:
        in_board = True
        for i in range(len(word) - 1):
            if (
                    word[i: i+2] not in seq_two
                    and word[i+1] + word[i] not in seq_two
            ):
                in_board = False
                break
        if not in_board:
            continue
        if word[:4] == word[0] * 4:
            word = word[::-1]
            reversed_words.add(word)
        candidates.append(word)
    num_rows, num_cols = len(board), len(board[0])
    res = set()
    trie = Trie(candidates)

    def dfs(row: int, col: int, current: list[str]) -> None:
        current.append(board[row][col])
        board[row][col] = "."
        found = trie.contains(current)
        if not found:
            board[row][col] = current.pop()
            return
        if found == 2:
            w = "".join(current)
            if w in reversed_words:
                res.add(w[::-1])
                reversed_words.remove(w)
            else:
                res.add(w)
            trie.remove(w)
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for di, dj in dirs:
            i, j = row + di, col + dj
            if (
                    0 <= i < num_rows
                    and 0 <= j < num_cols
                    and board[i][j] != "."
            ):
                dfs(i, j, current)
        # Backtrack
        board[row][col] = current.pop()
    for i in range(num_rows):
        for j in range(num_cols):
            dfs(i, j, [])
    return res


def main():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(find_words(board, words))


if __name__ == "__main__":
    main()
