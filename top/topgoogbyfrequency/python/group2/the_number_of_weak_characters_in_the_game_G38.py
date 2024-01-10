"""
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack
 and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the
  properties of the ith character in the game.
A character is said to be weak if any other character has both attack and defense levels strictly greater than this
 character's attack and defense levels. More formally, a character i is said to be weak if there exists another
  character j where attackj > attacki and defensej > defensei.
Return the number of weak characters.

Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Constraints:
2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5
"""


def number_of_weak_characters(properties: list[list[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))

    ans = 0
    curr_max = 0

    for _, d in properties:
        if d < curr_max:
            ans += 1
        else:
            curr_max = d
    return ans


def number_of_weak_characters1(properties: list[list[int]]) -> int:
    properties.sort(key=lambda x: (x[0], -x[1]))

    stack = []
    ans = 0

    for a, d in properties:
        while stack and stack[-1] < d:
            stack.pop()
            ans += 1
        stack.append(d)
    return ans


def main():
    properties = [[5, 5], [6, 3], [3, 6]]
    print(number_of_weak_characters1(properties))


if __name__ == "__main__":
    main()
