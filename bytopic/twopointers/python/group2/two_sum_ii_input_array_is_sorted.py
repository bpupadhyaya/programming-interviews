"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Tag: 27/150
Tag: 167/2927, R570/2936 (overall frequency ranking)
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1
    while numbers[i] + numbers[j] != target:
        s = numbers[i] + numbers[j]
        if s > target:
            j -= 1
        else:
            i += 1
    return [i+1, j+1]


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))


if __name__ == "__main__":
    main()
