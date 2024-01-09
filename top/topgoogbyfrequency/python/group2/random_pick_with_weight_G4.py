"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive)
 and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of
 picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Tag: fb R13/50, 528/2927, R192/2936, G4/50
"""


# from typing import List
import random


class Solution:
    def __init__(self, w: list[int]):
        self.w = w
        # 1. calculate relative frequency
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        # 2. put relative frequencies on the number lines between 0 and 1. Note: self.w[-1] = 1
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]

    def pick_index(self) -> int:
        # this is where we pick the index
        N = random.uniform(0,1)

        flag = 1
        index = -1

        # test each region of the number line to see if N falls in it, if it
        # does not then go to the next index and check if N falls in it
        # this is guaranteed to break because of previous normalization

        while flag:
            index += 1
            if N <= self.w[index]:
                flag = 0

        return index


def main():
    solution = Solution([1, 3])
    print(solution.pick_index())  # return 1. It is returning the second element (index = 1) that has a
    # probability of 3/4.
    print(solution.pick_index())  # return 1
    print(solution.pick_index())  # return 1
    print(solution.pick_index())  # return 1
    print(solution.pick_index())  # return 0. It is returning the first element (index = 0) that has a
    # probability of 1/4.


if __name__ == "__main__":
    main()

