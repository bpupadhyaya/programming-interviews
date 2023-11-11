// Given a string s, find the length of the longest substring without repeating characters.
// Example 1: Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//  Example 2:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Tag: 31/150

#include <iostream>
#include <vector>

using namespace std;

 int length_of_longest_substring(string s) {
    int n = s.length();
    int max_length = 0;
    vector<int> char_index(128, -1);
    int left = 0;

    for (int right = 0; right < n; right++) {
        if (char_index[s[right]] >= left) {
            left = char_index[s[right]] + 1;
        }
        char_index[s[right]] = right;
        max_length = max(max_length, right - left + 1);
    }
    return max_length;
 }

 int main() {
    string s = "pwwkew";
    cout << length_of_longest_substring(s) << "\n";
 }

// Steps:
//  Integer Array approach:
// 1. This solution uses an integer array charIndex to store the indices of characters.
// 2. We eliminate the need for an unordered map by utilizing the array.
// 3. The max_length, left, and right pointers are still present.
// 4. We iterate through the string using the right pointer.
// 5. We check if the current character has occurred within the current substring by comparing its index in charIndex with left.
// 6. If the character has occurred, we move the left pointer to the next position after the last occurrence of the character.
// 7. We update the index of the current character in charIndex.
// 8. At each step, we update the max_length by calculating the length of the current substring.
// 9. We continue the iteration until reaching the end of the string.
// 10. Finally, we return the max_length as the length of the longest substring without repeating characters.