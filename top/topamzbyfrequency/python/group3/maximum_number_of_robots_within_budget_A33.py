"""
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n.
The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given
an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where
max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running
costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.

Example:
Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
Output: 3
Explanation:
It is possible to run all individual and consecutive pairs of robots within budget.
To obtain answer 3, consider the first 3 robots. The total cost will be
max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.

Tag: 2398/2927 , R931/2935 , R33/50 (amz)
"""


def maximum_robots(charge_times: list[int], running_costs: list[int], budget: int) -> int:
    n = len(charge_times)
    start = 0
    running_sum = 0
    max_consecutive = 0
    max_so_far = 0
    second_max = 0

    for end in range(n):
        running_sum += running_costs[end]

        if max_so_far <= charge_times[end]:
            second_max = max_so_far
            max_so_far = charge_times[end]

        k = end - start + 1

        current_budget = max_so_far + (k * running_sum)

        if current_budget > budget:
            running_sum -= running_costs[start]
            max_so_far = second_max if charge_times[start] == max_so_far else max_so_far
            start += 1

        max_consecutive = max(max_consecutive, end - start + 1)

    return max_consecutive


def main():
    charge_times = [3, 6, 1, 3, 4]
    running_costs = [2, 1, 3, 4, 5]
    budget = 25
    print(maximum_robots(charge_times, running_costs, budget))


if __name__ == "__main__":
    main()
