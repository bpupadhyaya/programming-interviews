"""
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.

Example:
Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab".
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.

Tag: 2193/2927 , R323/2935 , R17/50 (amz)
"""


def min_moves_to_make_palindrome_using_string_peel(s: str) -> int:
    ans = 0
    while len(s) > 2:
        lo = s.find(s[-1])
        hi = s.rfind(s[0])
        if lo < len(s) - hi - 1:
            ans += lo
            s = s[:lo] + s[lo+1:-1]
        else:
            ans += len(s) - hi - 1
            s = s[1:hi] + s[hi+1:]
    return ans


def min_moves_to_make_palindrome_using_two_pointer(s: str) -> int:
    l, r, res, st = 0, len(s) - 1, 0, list(s)
    while l < r:
        if st[l] != st[r]:
            i = r
            while i > l and st[l] != st[i]:
                i -= 1
            if i == l:
                st[i], st[i+1] = st[i+1], st[i]
                res += 1
                continue
            else:
                while i < r:
                    st[i], st[i+1] = st[i+1], st[i]
                    i += 1
                    res += 1
        l, r = l+1, r-1
    return res


def main():
    s = "aabb"
    print(min_moves_to_make_palindrome_using_two_pointer(s))


if __name__ == "__main__":
    main()


"""
Explanation for two pointer:
At each point, we look at the first and the last elements
if they are the same, then we skip them, else we find
another element in the string that matches the left
element and then we make the necessary swaps to move it
to the right place. 
if we can't find that element -- this means this is the middle element
in the palindrome, we just move it one position to the right and continue
over the next few iterations, it will be moved to the center automatically
run it for string = "dpacacp", answer should be 4
the character that should be in the middle is "d"
"""