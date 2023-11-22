"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Tag: fb R38/50, 670/2927, R862/2936
"""


def maximum_swap(num: int) -> int:
    s = list(str(num))
    n = len(s)
    for i in range(n-1):  # chance to flip
        if s[i] < s[i+1]:
            break
        else:
            return num
    max_idx, max_val = i+1, s[i+1]  # keep going right, find the max. value point
    for j in range(i+1, n):
        if max_val <= s[j]:
            max_idx, max_val = j, s[j]
    left_idx = i  # going right from i, find the left most value that is less than max_val
    for j in range(i, -1, -1):
        if s[j] < max_val:
            left_idx = j
    s[max_idx], s[left_idx] = s[left_idx], s[max_idx]  # swap max. after i and (most) left  less than max
    return int(''.join(s))  # re-create the integer


def main():
    num = 2736
    print('Resulting number: ', maximum_swap(num))


if __name__ == "__main__":
    main()

