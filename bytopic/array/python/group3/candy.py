"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Tag: 15/150
Tag: 135/2927, R87/2936 (overall frequency ranking)
"""


def candy(ratings: list[int]) -> int:
    if not ratings:
        return 0

    ret, up, down, peak = 1, 0, 0, 0

    for prev, curr in zip(ratings[:-1], ratings[1:]):
        if prev < curr:
            up, down, peak = up + 1, 0, up + 1
            ret += 1 + up
        elif prev == curr:
            up = down = peak = 0
            ret += 1
        else:
            up, down = 0, down + 1
            ret += 1 + down - int(peak >= down)

    return ret


def main():
    ratings = [1, 2, 2]
    print(candy(ratings))


if __name__ == "__main__":
    main()

"""
Time and Space Complexity
Time Complexity: O(n), for the single pass through the ratings array.
Space Complexity: O(1), as we only use a few extra variables.
"""
