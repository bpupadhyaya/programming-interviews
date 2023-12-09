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

Algo:
1. Initialize Your Counters
Start with ret = 1 because each child must have at least one candy. Initialize up, down, and peak to 0.

2. Loop Through Ratings
For each pair of adjacent children, compare their ratings. Here are the scenarios:
- If the rating is increasing: Update up and peak by incrementing them by 1. Set down to 0. Add up + 1 to ret because 
the current child must have one more candy than the previous child.
- If the rating is the same: Reset up, down, and peak to 0, because neither an increasing nor a decreasing trend is 
maintained. Add 1 to ret because the current child must have at least one candy.
- If the rating is decreasing: Update down by incrementing it by 1. Reset up to 0. Add down to ret. Additionally, if 
peak is greater than or equal to down, decrement ret by 1. This is because the peak child can share the same number 
of candies as one of the children in the decreasing sequence, which allows us to reduce the total number of candies.

3. Return the Total Candy Count
- At the end of the loop, ret will contain the minimum total number of candies needed for all the children, 
so return ret. By using up, down, and peak, we can efficiently traverse the ratings list just once, updating our 
total candies count (ret) as we go. This method is efficient and helps us solve the problem in a single pass, 
with a time complexity of O(n).
"""
