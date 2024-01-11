"""
You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number such that the value of the
 resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least
  once in number.

Example 1:
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".

Constraints:
2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number.

Tag: M47/50
"""


def remove_digit(number: str, digit: str) -> str:
    # Initializing the last index as zero
    last_index = 0

    # Iterating each number to find the occurrences,
    # and to find if the number is greater than the next element

    for num in range(1, len(number)):

        # Handling [case 1] and [case 2]
        if number[num-1] == digit:
            if int(number[num]) > int(number[num-1]):
                return number[:num-1] + number[num:]
            else:
                last_index = num - 1

    # If digit is the last number (last occurrence) in the string [case 3]
    if number[-1] == digit:
        last_index = len(number) - 1

    return number[:last_index] + number[last_index + 1:]


def main():
    number = "123"
    digit = "3"
    print(remove_digit(number, digit))


if __name__ == "__main__":
    main()

