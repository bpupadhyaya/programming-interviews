"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any
two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".

Tag: G15/50
"""


def find_min_difference(time_points: list[str]) -> int:
    def minute(time_: str) -> int:
        h, m = map(int, time_.split(':'))
        return 60*h + m

    M = 1440
    times = [False] * M
    for time in time_points:
        mnt = minute(time)
        if times[mnt]:
            return 0
        times[mnt] = True

    minutes = [i for i in range(M) if times[i]]
    return min((minutes[i] - minutes[i-1]) % M for i in range(len(minutes)))


def main():
    time_points = ["23:59", "00:00"]
    print(find_min_difference(time_points))


if __name__ == "__main__":
    main()
