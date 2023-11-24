"""
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on
the ith shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n.
For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.

Example 1:
Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.

Example 2:
Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.


Tag: 2355/2927 , R523/2935 , R25/50 (amz)
"""
from typing import List


def maximum_books(books: List[int]) -> int:
    n = len(books)
    dp, stack = [0] * n, []
    for i in range(n):
        if books[i] == 0:
            stack.append(i)
            continue
        while stack:
            j = stack[-1]
            if books[j] >= books[i] - (i - j):
                stack.pop()
            else:
                break
        if not stack:
            j = -1
        if books[i] - i + j + 1 < 0:
            dp[i] = books[i] * (books[i] + 1) // 2
        else:
            dp[i] = (books[i] + books[i] - i + j + 1) * (i - j) // 2
        if j >= 0:
            dp[i] += dp[j]
        stack.append(i)
    return max(dp)


def main():
    books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]
    print(maximum_books(books))


if __name__ == "__main__":
    main()

"""
Implementation explanation:
DP and Stack, O(N):
Step 1: Create a dp array where dp[i] is the maximum number of books that we can take from bookshelves 0 to i and
we must take all books from bookshelf i.
Step 2: Keep taking as many books as we can (i.e. starting from bookshelf i and going backwards, you
take arr[i], arr[i] - 1, arr[i] - 2, …, books).
Step 3: Keep a stack of possible indices for j. If x is the number at the top of the stack, keep popping from
the stack while arr[x] ≥ arr[i] - (i - x). This is because if the inequality mentioned before is true, x will 
never be an index j as index i will run out of items first.
"""