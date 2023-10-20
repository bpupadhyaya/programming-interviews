// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Sample 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"

import java.util.Arrays;
class LongestCommonPrefix {
    public static void main(String...args) {
        String[] strs = {"flower","flow","flight"};
        System.out.println("Longest...: " + longestCommonPrefix(strs));
    }

    static String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length - 1];
        int idx = 0;
        while (idx < s1.length() && idx < s2.length()) {
            if (s1.charAt(idx) == s2.charAt(idx)) {
                idx++;
            } else {
                break;
            }
        }
        return s1.substring(0, idx);
    }
}

