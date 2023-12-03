"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Mapping from phone pad:
1 (none), 2(abc), 3(def), 4(ghi), 5(jkl), 6(mno), 7(pqrs), 8(tuv), 9(wxyz)

Sample 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Tag: 101/150
Tag: 17/2927, R36/2936 (overall frequency ranking)
"""


def letter_combination(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    backtrack("", digits)
    return output


def main():
    digits = "23"
    print(letter_combination(digits))


if __name__ == "__main__":
    main()
