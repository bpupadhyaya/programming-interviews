"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Tag: 767/2927 , R41/2935 , R5/50 (amz)

Note: pq method doesn't produce correct output, debug and fix it.
"""

import heapq


def reorganize_string_using_pq(s: str) -> str:
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res.extend([char1, char2])

            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res.append(char)
        return "".join(res)


def reorganize_string_using_array_sort(s: str) -> str:
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

    if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
        return ""

    res = [None] * len(s)

    i = 0
    for char in sorted_chars:
        for _ in range(freq_map[char]):
            if i >= len(s):
                i = 1
            res[i] = char
            i += 2
    return "".join(res)


def main():
    s = "aab"
    print(reorganize_string_using_array_sort(s))


if __name__ == "__main__":
    main()
