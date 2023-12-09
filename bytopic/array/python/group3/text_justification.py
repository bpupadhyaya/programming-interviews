"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth
characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra
spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does
not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Tag: 24/150
Tag: 68/2927, R50/2936 (overall frequency ranking), R1/50 (goog)
"""


def full_justify(words: list[str], max_width: int) -> list[str]:
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(max_width)]


def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    print(full_justify(words, max_width))


if __name__ == "__main__":
    main()


"""
Note on implementation:
From the question: the sentence "Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned 
more spaces than the slots on the right" was just a really long and awkward way to say round robin. 
The following line implements the round robin logic:

for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
What does this line do? Once you determine that there are only k words that can fit on a given line, you 
know what the total length of those words is num_of_letters. Then the rest are spaces, and there 
are (maxWidth - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1.
"""
