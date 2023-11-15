// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
// characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
// while "aec" is not).
// Example:
// Input: s = "abc", t = "ahbgdc"
// Output: true
//
// Tag: 26/150
// Tag: 392/2927, R348/2936 (overall frequency ranking)

class SubsequenceDetection {
    public static void main(String[] args) {
        String s = "abc";
        String t = "ahbgdc";
        System.out.println("Subsequence? " + isSubsequence(s,t));
    }

    static boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == s.length();
    }
}

// Two Pointers Approach:
// The two-pointers technique is an iterative approach that uses two indices, one for each string. The idea is to traverse
// the longer string t and whenever a character matches the current character of string s, the index for s is moved to the right.
// Key Data Structures:
// i and j: Two pointers initialized to 0. i is used for string s and j for string t.
// Steps:
// 1. Traverse and Match:
// -Traverse string t using pointer j.
// -If the current character of t matches the current character of s, increment i.
// -Continue until the end of string t or until all characters of s are found in t.
// 2. Check Subsequence:
// -At the end of traversal, if i is equal to the length of s, then s is a subsequence of t.
//
// Complexity Analysis:
// Time Complexity:
// The algorithm traverses the string t once, resulting in a time complexity of O(len(t)).
// Space Complexity:
// Constant space is used, leading to a space complexity of O(1).
