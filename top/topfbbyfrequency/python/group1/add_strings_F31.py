"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Tag: F31/50
Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


def add_strings(num1: str, num2: str) -> str:
    # using dictionary / hashmap
    def str2int(num):
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                    '6': 6, '7': 7, '8': 8, '9': 9}
        output = 0
        for d in num:
            output = output * 10 + num_dict[d]
        return output

    return str(str2int(num1) + str2int(num2))


def add_strings1(num1: str, num2: str) -> str:
    # using unicode
    def str2int(num):
        result = 0
        for n in num:
            result = result * 10 + ord(n) - ord('0')
        return result
    return str(str2int(num1) + str2int(num2))


def main():
    num1 = "11"
    num2 = "123"
    print(add_strings1(num1, num2))


if __name__ == "__main__":
    main()
