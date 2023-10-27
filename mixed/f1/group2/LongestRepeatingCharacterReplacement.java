// You are given a string s and an integer k. You can choose any character of the string and change it to any other
// uppercase English character. You can perform this operation at most k times.
// Return the length of the longest substring containing the same letter you can get after performing the above operations.
// Sample 1:
// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
// The substring "BBBB" has the longest repeating letters, which is 4.
// There may exists other ways to achieve this answer too.

class LongestRepeatingCharacterReplacement {
    public static void main(String...args) {
        String s = "AABABBA";
        int k = 1;
        System.out.println("Length... after replacement: " + characterReplacement(s, k));
    }

    static int characterReplacement(String s, int k) {
        int[] arr = new int[26];
        int largestCount = 0, beg = 0, maxLen = 0;
        for (int end = 0; end < s.length(); end++) {
            arr[s.charAt(end) - 'A']++;
            largestCount = Math.max(largestCount, arr[s.charAt(end) - 'A']);
            if (end - beg + 1 - largestCount > k) {
                arr[s.charAt(beg) - 'A']--;
                beg++;
            }
            maxLen = Math.max(maxLen, end - beg + 1);
        }
        return maxLen;
    }
}