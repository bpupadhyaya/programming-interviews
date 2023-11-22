"""
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k.
You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
- Keep the ribbon of length 4,
- Cut it into one ribbon of length 3 and one ribbon of length 1,
- Cut it into two ribbons of length 2,
- Cut it into one ribbon of length 2 and two ribbons of length 1, or
- Cut it into four ribbons of length 1.

Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess
  ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain
k ribbons of the same length.

Example 1:
Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.

Example 2:
Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.

Tag: fb R50/50, 1891/2927, R2091/2936.
"""


def max_length(ribbons: list[int], k: int) -> int:
    # The minimum length of the ribbon that we can cut is 1
    start = 1
    # The maximum length of the ribbon can be the maximum element in the list
    end = max(ribbons)

    # In this binary search, we are trying to go through the original list and figure out which integer (1 to
    # ribbon of max length) is the desired length for hte target k pieces.
    while start <= end:
        mid = start + (end - start) // 2
        res = 0
        for i in ribbons:
            res += i // mid
        # If the value is >= target, we know that there could be larger integer that will satisfy the same condition
        if res >= k:
            start = mid + 1
        else:
            # If lesser than k, then there could be a value lesser than the mid that could satisfy the condition
            end = mid - 1
    return end


def main():
    ribbons = [9,7,5]
    k = 3
    print('Max length: ', max_length(ribbons, k))


if __name__ == "__main__":
    main()
