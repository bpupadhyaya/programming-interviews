"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
 "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e",
  "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

"""
import re


def is_number(s: str) -> bool:
    engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
    return engine.match(s.strip(" "))


def is_number1(s: str) -> bool:
    try:
        if s == "inf" or s == "-inf" or s == "+inf" or s == "Infinity" or s == "infinity" \
                or s == "+Infinity" or s == "-Infinity" or s == "+infinity" or s == "-infinity" or s == "nan":
            return 0
        num = float(s)
        return 1
    except:
        return 0


def is_number2(s: str) -> bool:
    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
    return bool(pattern.match(s))


def main():
    s = "0"
    print(is_number2(s))


if __name__ == "__main__":
    main()
