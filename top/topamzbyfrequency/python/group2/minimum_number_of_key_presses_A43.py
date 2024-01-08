"""
You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters.
You can choose which characters each button is matched to as long as:
- All 26 lowercase English letters are mapped to.
- Each character is mapped to by exactly 1 button.
- Each button maps to at most 3 characters.

To type the first character matched to a button, you press the button once. To type the second character,
you press the button twice, and so on.
Given a string s, return the minimum number of keypresses needed to type s using your keypad.
Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.

Example:
Note: keypad visualization: 3 x 3 matrix: {{1,2,3}{4,5,6}{7,8,9}} with below character mapping:
{{1-> {ajs}}, {2 -> {bkt}}, {3 -> {clu}}, {4 -> {dmv}}, {5 -> {enw}}, {6 -> {fox}}, {7 -> {gpy}}, {8 -> {hqz}},
{9 -> {ir}}}
Input: s = "abcdefghijkl"
Output: 15
Explanation: One optimal way to setup your keypad is shown above.
The letters 'a' to 'i' can each be typed by pressing a button once.
Type 'j' by pressing button 1 twice.
Type 'k' by pressing button 2 twice.
Type 'l' by pressing button 3 twice.
A total of 15 button presses are needed, so return 15.

Tag: 2268/2927 , R1744/2935 , R43/50 (amz)
"""

import collections


def minimum_key_presses(s: str) -> int:
    c = collections.Counter(s)
    ans = count = 0
    for i, freq in enumerate(sorted(c.values(), reverse=True)):  # sort in reverse order
        if i % 9 == 0:
            count += 1
        ans += count * freq
    return ans


def main():
    s = "abcdefghijkl"
    print(minimum_key_presses(s))


if __name__ == "__main__":
    main()
