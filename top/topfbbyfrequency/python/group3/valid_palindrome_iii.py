"""
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.
Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:
Input: s = "abbababa", k = 1
Output: true

Tag: fb R49/50, 1216/2927, R2055/2936
"""


def is_valid_palindrome(s: str, k: int) -> bool:
    dp = [[0 for _ in s] for _ in s]

    for i in range(len(dp)-1, -1, -1):
        for j in range(i+1, len(dp)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(1 + dp[i][j-1], 1 + dp[i+1][j], 2 + dp[i+1][j-1])

    # print(dp)
    return dp[0][-1] <= k


def main():
    s = "abcdeca"
    k = 2
    print("Is valid palindrome? " + str(is_valid_palindrome(s, k)))


if __name__ == "__main__":
    main()


"""
 APPROACH : DP ##
 LOGIC ##
 1. Draw Bottom Up DP Table
      a) when length == 1, no change required, so dp[i][j] = 0
      b) when length == 2, if string is aa or bb, we do not require any k, so take previous substring value i.e. from
       diagonal. else we take as 1. i.e. we require 1 char to change
      c) when length > 2, we can generalize it as, if s[i] == s[j] then we can remove ith character which requires
       one operation and take previous s[i+1][j] value or 1 + dp[i][j-1] or we remove both chars take previous
        substring i.e 2 + dp[i+1][j-1]

  STACK TRACE ##
  Example:  s = "abcdeca"
  
  [
      [0, 1, 2, 3, 4, 3, 2], 
      [0, 0, 1, 2, 3, 2, 3], 
      [0, 0, 0, 1, 2, 1, 2], 
      [0, 0, 0, 0, 1, 2, 3], 
      [0, 0, 0, 0, 0, 1, 2], 
      [0, 0, 0, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 0, 0]
  ]
  
"""