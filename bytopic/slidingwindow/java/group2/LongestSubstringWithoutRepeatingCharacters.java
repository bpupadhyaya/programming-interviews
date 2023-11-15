// Given a string s, find the length of the longest substring without repeating characters.
// Example 1: Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//  Example 2:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
// Tag: 31/150
// // Tag: 3/2927, R8/2936 (overall frequency ranking)

import java.util.Arrays;
class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String...args) {
        String s = "pwwkew";
        System.out.println("Length of longest substring: " + lengthOfLongestSubstring(s));
    }

    static int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, - 1);
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (charIndex[s.charAt(right)] >= left) {
                left = charIndex[s.charAt(right)] + 1;
            }
            charIndex[s.charAt(right)] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}

// Steps:
//  Integer Array approach:
// 1. This solution uses an integer array charIndex to store the indices of characters.
// 2. We eliminate the need for an unordered map by utilizing the array.
// 3. The maxLength, left, and right pointers are still present.
// 4. We iterate through the string using the right pointer.
// 5. We check if the current character has occurred within the current substring by comparing its index in charIndex with left.
// 6. If the character has occurred, we move the left pointer to the next position after the last occurrence of the character.
// 7. We update the index of the current character in charIndex.
// 8. At each step, we update the maxLength by calculating the length of the current substring.
// 9. We continue the iteration until reaching the end of the string.
// 10. Finally, we return the maxLength as the length of the longest substring without repeating characters.