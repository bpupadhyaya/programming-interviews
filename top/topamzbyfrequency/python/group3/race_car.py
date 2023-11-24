"""
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions.
Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed
goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

Example 1:
Input: target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:
Input: target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.



Tag: 818/2927 , R457/2935 , R22/50 (amz)

Note: DP implementation has incorrect output, debug and fix it.
"""
import math
from collections import deque
from functools import cache


def race_car(target: int) -> int:
    q = deque([(0, 1, 0)])  # curr pos, curr speed, number of moves

    while q:
        cp, cs, nm = q.popleft()

        if cp == target:
            return nm

        # In every pos, we have two choices: A or R
        # Accelerate
        q.append((cp + cs, cs * 2, nm + 1))

        # Reverse
        if (cp + cs > target and cs > 0) or (cp + cs < target and cs < 0):
            if cs < 0:
                q.append((cp, 1, nm + 1))
            else:
                q.append((cp, -1, nm + 1))


def race_car_bfs(target: int) -> int:
    # O(t*log(t))
    q = deque([(0, 1)])
    visited = set([0, 1])
    actions = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, v = q.popleft()
            if x == target:
                return actions

            # Accelerate
            # NOTE: if accelerating in the negative regions or passing the target by more than two times,
            # then this is never going to reach an answer, we won't add it to the queue
            newx = x + v
            newv = v * 2
            if 0 <= newx <= 2 * target and (state := (newx, newv)) not in visited:
                visited.add(state)
                q.append(state)

            # Reverse
            newv = -1 if v > 0 else 1
            if (state := (x, newv)) not in visited:
                visited.add(state)
                q.append(state)
        actions += 1


def race_car_dp(target: int) -> int:
    # O(t*log(t))

    @cache
    def go(n):
        m = n.bit_length()
        # check if we can go directly to the target
        if 2 ** m - 1 == n:
            return m
        else:
            # otherwise we have two choices
            # we pass the point, and then we reverse (denoted by passing_moves)
            # or we go as close to the target as possible, reverse, go back up to m - 2 times, reverse again,
            # and reach the point
            # note if we go back m - 1 times, we have reached the same point we started at.

            # 1. go past target (m moves), reverse (1 move), and reach the target
            passing_moves = m + 1 + go(2 ** m - 1 - n)
            # 2. go as close to target as possible (m -1 moves), reverse (1 move)
            closest_point = 2 ** (m - 1) - 1
            closest_move = m - 1
            min_ = math.inf
            for i in range(m - 1):
                backward = 2 ** i - 1
                remain_moves = go(n - (closest_point - backward)) + i
                min_ = min(min_, remain_moves)

            closest_move += min_ + 2

            return min(passing_moves, closest_move)

        return go(target)


def main():
    target = 6
    print(race_car_dp(target))


if __name__ == "__main__":
    main()

