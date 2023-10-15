// Given two strings s and t of lengths m and n respectively, return the minimum window substring
// of s such that every character in t, including duplicates, is included in the window. If there
// is no such substring, return the empty string.
// Sample 1:
// Input: s = "zxabtmcyno", t = "xyz"
// Output: "zxabtmcy"
// Explanation: The minimum window substring "zxabtmcy" includes 'x', 'y', and 'c' from string t.

class MinimumWindowSubstring {
    public static void main(String...args){
        String myInput = "zxabtmcyno";
        String t = "xyz";
        System.out.println("Minimum widow substring: " + findMinimumWindowSubstring(myInput, t));
    }

    static String findMinimumWindowSubstring(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) {
            return "";
        }

        int[] map = new int[128];
        int count = t.length();
        int start = 0, end = 0, minLen = Integer.MAX_VALUE, startIndex = 0;
        for(char c: t.toCharArray()) {
            map[c]++;
        }
        char[] chS = s.toCharArray();
        while (end < chS.length) {
            if (map[chS[end++]]-- > 0) {
                count--;
            }
            while (count == 0) {
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }
                if (map[chS[start++]]++ == 0) {
                    count++;
                }
            }
        }

        return minLen == Integer.MAX_VALUE? "" : new String(chS, startIndex, minLen);
    }
}