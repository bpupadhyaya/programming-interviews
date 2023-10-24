// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
// space-separated sequence of one or more dictionary words.
// Note that the same word in the dictionary may be reused multiple times in the segmentation.
// Sample 1:
// Input: s = "applepenapple", wordDict = ["apple","pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
// Note that you are allowed to reuse a dictionary word.
// Soln: dynamic programming

import java.util.Arrays;
import java.util.List;
class WordBreak {
    public static void main(String...args) {
        String s = "applepenapple";
        List<String> wordDict = Arrays.asList(new String[]{"apple","pen"});
        System.out.println("Can be segmented? " + wordBreak(s, wordDict));
    }

    static boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n+1];
        dp[0] = true;
        int maxLen = 0;
        for (String word: wordDict) {
            maxLen = Math.max(maxLen, word.length());
        }

        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j >= Math.max(i - maxLen - 1, 0); j--) {
                if (dp[j] && wordDict.contains(s.substring(j,i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}