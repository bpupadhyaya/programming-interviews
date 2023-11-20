"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Tag: 680/2927, R97/2936 (overall), fb R6/50,
"""

def validPalindrome(s: str) -> bool:
    def verify(s, left, right, deleted):
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return verify(s, left+1, right, True) or verify(s, left, right-1, True)
            else:
                left += 1
                right -= 1
        return True;
    return verify(s, 0, len(s)-1, False)

def main():
    s = "abca"
    print('Result: ', validPalindrome(s))

if __name__ == "__main__":
    main()
