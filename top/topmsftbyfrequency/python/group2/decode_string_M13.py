"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are
well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits
 are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Tag: M13/50
"""


def decode_string(s: str) -> str:
    def dfs(s, p):
        res = ""
        i, num = p, 0
        while i < len(s):
            asc = (ord(s[i])-48)
            if 0 <= asc <= 9:           # can also be written as if s[i].isdigit()
                num = num*10+asc
            elif s[i] == "[":
                local, pos = dfs(s, i+1)
                res += local*num
                i = pos
                num = 0
            elif s[i] == "]":
                return res, i
            else:
                res += s[i]
            i += 1
        return res, i

    return dfs(s, 0)[0]


def decode_string1(s: str) -> str:
    stack = []
    cur_num = 0
    cur_string = ''
    for c in s:
        if c == '[':
            stack.append(cur_string)
            stack.append(cur_num)
            cur_string = ''
            cur_num = 0
        elif c == ']':
            num = stack.pop()
            prev_string = stack.pop()
            cur_string = prev_string + num*cur_string
        elif c.isdigit():     # cur_num*10+int(c) is helpful in keep track of more than 1 digit number
            cur_num = cur_num*10 + int(c)
        else:
            cur_string += c
    return cur_string


def main():
    s = "3[a]2[bc]"
    print(decode_string1(s))


if __name__ == "__main__":
    main()
