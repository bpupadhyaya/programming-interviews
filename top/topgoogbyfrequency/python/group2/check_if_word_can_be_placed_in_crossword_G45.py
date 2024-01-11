"""
You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains
 lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked
  cells.
A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top)
 in the board if:
It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was
 placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was
 placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

Example:
Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).

Constraints:
m == board.length
n == board[i].length
1 <= m * n <= 2 * 10^5
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.

Tag: G45/50
"""
from itertools import chain, product


def place_word_in_crossword(board: list[list[str]], word: str) -> bool:
    n, words = len(word), [word, word[::-1]]
    for brd in (board, zip(*board)):
        brd = chain(*[''.join(row).split('#') for row in brd])
        for s, w in product(brd, words):
            if len(s) == n and all(s[i] in [' ', w[i]] for i in range(n)):
                return True

    return False


def main():
    board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
    word = "abc"
    print(place_word_in_crossword(board, word))


if __name__ == "__main__":
    main()
