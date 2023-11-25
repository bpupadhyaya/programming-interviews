"""
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s
consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the
substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that
are in the substring. A plate is considered between candles if there is at least one candle to its left and at least
one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between
candles in this substring is 2, as each of the two plates has at least one candle in the substring to
its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

Tag: 2055/2927 , R635/2935 , R29/50 (amz)
"""
import bisect


def plates_between_candles_using_bisect(s: str, queries: list[list[int]]) -> list[int]:
    p = [i for i in range(len(s)) if s[i] == '|']

    res = []
    for f, t in queries:
        left = bisect.bisect_left(p, f)
        right = bisect.bisect_right(p, t)
        res.append(p[right-1] - p[left] - (right-1-left) if right > left else 0)

    return res


def plates_between_candles_using_binary_search(s: str, queries: list[list[int]]) -> list[int]:
    prefix = [0]
    candles = []
    for i, ch in enumerate(s):
        if ch == '|':
            candles.append(i)
        if ch == '|':
            prefix.append(prefix[-1])
        else:
            prefix.append(prefix[-1] + 1)

    ans = []
    for x, y in queries:
        lo = bisect.bisect_left(candles, x)
        hi = bisect.bisect_right(candles, y) - 1
        if 0 <= hi and lo < len(candles) and lo <= hi:
            ans.append(prefix[candles[hi] + 1] - prefix[candles[lo]])
        else:
            ans.append(0)
    return ans


def main():
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    print(plates_between_candles_using_bisect(s, queries))


if __name__ == "__main__":
    main()

