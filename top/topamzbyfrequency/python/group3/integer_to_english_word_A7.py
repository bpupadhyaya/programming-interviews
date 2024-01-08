"""
Convert a non-negative integer num to its English words representation.
Example:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Tag: 273/2927 , R62/2935 , R7/50 (amz)
"""


def number_to_words(num: int) -> str:
    if num == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
             "Eighteen", "Nineteen"]
    suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion",
                "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
    words = []
    i = 0

    while num > 0:
        triplet = num % 1000
        num = num // 1000
        if triplet == 0:
            i += 1
            continue
        temp = []
        if triplet // 100 > 0:
            temp.append(ones[triplet // 100])
            temp.append("Hundred")
        if 10 <= triplet % 100 <= 19:
            temp.append(teens[triplet % 10])
        else:
            if triplet % 100 >= 20:
                temp.append(tens[triplet % 100 // 10])
            if triplet % 10 > 0:
                temp.append(ones[triplet % 10])
        if i > 0:
            temp.append(suffixes[i])
        words = temp + words
        i += 1
    return " ".join(words)


def main():
    num = 1234567
    print(number_to_words(num))


if  __name__ == "__main__":
    main()