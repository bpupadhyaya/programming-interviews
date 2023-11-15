// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
//
// Tag: 20/150
// Tag: 14/2927, R13/2936 (overall frequency ranking)

import java.util.Arrays;
class LongestCommonPrefix {
    public static void main(String...args) {
        String[] s = {"flower","flow","flight"};
        System.out.println("Longest common prefix: " + longestCommonPrefix(s));
    }

    static String longestCommonPrefix(String[] s) {
        StringBuilder ans = new StringBuilder();
        Arrays.sort(s);
        String first = s[0];
        String last = s[s.length - 1];
        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) != last.charAt(i)) {
                return ans.toString();
            }
            ans.append(first.charAt(i));
        }
        return ans.toString();
    }
}

// Steps:
// 1. Initialize an empty string ans to store the common prefix.
// 2. Sort the input list v lexicographically. This step is necessary because the common prefix should be common to all the strings,
// so we need to find the common prefix of the first and last string in the sorted list.
// 3. Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string.
// 4. If the current character of the first string is not equal to the current character of the last string, return the common prefix
// found so far.
// 5. Otherwise, append the current character to the ans string.
// 6. Return the ans string containing the longest common prefix.