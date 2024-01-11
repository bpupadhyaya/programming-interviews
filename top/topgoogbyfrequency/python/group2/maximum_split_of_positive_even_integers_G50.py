"""
You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.
For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up
 to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number
  of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
Return a list of integers that represent a valid split containing a maximum number of integers. If no valid
 split exists for finalSum, return an empty list. You may return the integers in any order.

Example 1:
Input: finalSum = 12
Output: [2,4,6]
Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.

Constraints:
1 <= finalSum <= 10^{10}


Tag: G50/50
"""


def maximum_even_split(final_sum: int) -> list[int]:
    ans, i = [], 2
    if final_sum % 2 == 0:
        while i <= final_sum:
            ans.append(i)
            final_sum -= i
            i += 2
        ans[-1] += final_sum
    return ans


def maximum_even_split1(final_sum: int) -> list[int]:
    ans = set()
    if final_sum % 2 != 0:
        return ans
    else:
        s = 0
        i = 2                       # even pointer 2, 4, 6, 8, 10, 12, ...
        while s < final_sum:
            s += i                # sum
            ans.add(i)      # append the i in list
            i += 2
        if s == final_sum:  # if sum s is equal to finalSum then no modification required
            return ans
        else:
            ans.discard(s - final_sum)  # Deleting the element which makes s greater than finalSum
            return ans


def main():
    final_sum = 12
    print(maximum_even_split(final_sum))


if __name__ == "__main__":
    main()
