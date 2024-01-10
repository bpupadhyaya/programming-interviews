"""
An attendance record for a student can be represented as a string where each character signifies whether the student
 was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible
 for an attendance award. The answer may be very large, so return it modulo 109 + 7.

Example 1:
Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Constraints:
1 <= n <= 10^5
"""


def check_record(n: int) -> int:
    """
    Suppose dp[i] is the number of all the rewarded sequences without 'A'
    having their length equals to i, then we have:
        1. Number of sequence ends with 'P': dp[i - 1]
        2. Number of sequence ends with 'L':
            2.1 Number of sequence ends with 'PL': dp[i - 2]
            2.2 Number of sequence ends with 'LL':
                2.2.1 Number of sequence ends with 'PLL': dp[i - 3]
                2.2.2 Number of sequence ends with 'LLL': 0 (not allowed)

        So dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3], 3 <= i <= n

    Then all the rewarding sequences with length n are divided into
    two cases as follows:
        1. Number of sequences without 'A': dp[n]
        2. Number of sequence with A in the middle, since we could only
            have at most one A in the sequence to get it rewarded,
            suppose A is at the ith position, then we have:
                A[i] = dp[i] * dp[n - 1 - i]

            Then the number of such sequences is:
                sum(A[i] for i in range(n))

    Then our final result will be dp[n] + sum(A[i] for i in range(n)).

    Corner cases:
        1. dp[0] = 1: which means the only case when the sequence is an
            empty string.
        2. dp[1] = 2: 'L', 'P'
        3. dp[2] = 4: 'LL', 'LP', 'PL', 'PP'
    """

    if not n:
        return 0

    if n == 1:
        return 3

    MOD = 10 ** 9 + 7
    dp = [1, 2, 4] + [0] * (n - 2)

    # Calculate sequences without 'A'.
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    # Calculate final result.
    result = dp[n] % MOD
    for i in range(n):
        result += (dp[i] * dp[n - 1 - i]) % MOD

    return result % MOD


def main():
    n = 2
    print(check_record(n))


if __name__ == "__main__":
    main()

