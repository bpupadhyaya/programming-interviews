"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
any letters.

{ {1 ->00}, {2 -> abc}, {3 -> def}, {4 -> ghi}, {5 -> jkl}, {6 -> mno}, {7 -> pqrs}, {8 -> tuv}, {9 -> wxyz}
}

Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Tag: Tag: R24/145
"""


def letter_combination(digits: str) -> list[str]:
    def backtrack(combination, next_digits):
        if not next_digits:
            res.append(combination)
            return
        for letter in phone[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])

    if not digits:
        return []
    phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    backtrack("", digits)
    return res


def main():
    digits = "23"
    print(letter_combination(digits))


if __name__ == "__main__":
    main()


"""
Algo:
We define a helper function "backtrack" that takes two arguments: the current combination and the remaining 
digits to process.

If there are no more digits to process, we append the current combination to the final list and return.

Otherwise, we iterate through each letter that the first remaining digit maps to, and recursively call the 
"backtrack" function with the new combination and the remaining digits.

We initialize the final list "res" to an empty list, and call the "backtrack" function with an empty 
combination and the original phone number.

Finally, we return the final list of combinations.
"""
