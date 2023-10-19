// We are given n different types of stickers. Each sticker has a lowercase English word on it.
// You would like to spell out the given string target by cutting individual letters from your collection
// of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite
// quantities of each sticker. Return the minimum number of stickers that you need to spell out target.
// If the task is impossible, return -1.
//Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and
// target was chosen as a concatenation of two random words.
// Sample 1:
// Input: stickers = ["with","example","science"], target = "thehat"
// Output: 3
// Explanation:
// We can use 2 "with" stickers, and 1 "example" sticker.
// After cutting and rearrange the letters of those stickers, we can form the target "thehat".
// Also, this is the minimum number of stickers necessary to form the target string.

import java.util.Map;
import java.util.HashMap;
class StickersToSpellWord {
    public static void main(String...args) {
        String[] stickers = {"with","example","science"};
        String target = "thehat";
        System.out.println("Min. number of stickers required: " + calculateMinimumNumberOfStickers(stickers, target));
    }

    static int calculateMinimumNumberOfStickers(String[] stickers, String target) {
        int m = stickers.length;
        int[][] mp = new int[m][26];
        Map<String, Integer> dp = new HashMap<>();
        for (int i = 0; i < m; i++)
            for (char c: stickers[i].toCharArray()) mp[i][c - 'a']++;
        dp.put("", 0);

        return helper(dp, mp, target);
    }

    private static int helper(Map<String, Integer> dp, int[][] mp, String target) {
        if (dp.containsKey(target))
            return dp.get(target);
        int ans = Integer.MAX_VALUE, n = mp.length;
        int[] tar = new int[26];
        for (char c: target.toCharArray())
            tar[c - 'a']++;
        for (int i = 0; i < n; i++) {
            if(mp[i][target.charAt(0) - 'a'] == 0)
                continue;
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < 26; j++) {
                if (tar[j] > 0)
                    for (int k = 0; k < Math.max(0, tar[j] - mp[i][j]); k++)
                        sb.append((char) ('a' + j));
            }
            String s = sb.toString();
            int tmp = helper(dp, mp, s);
            if (tmp != -1)
                ans = Math.min(ans, 1 + tmp);
        }
        dp.put(target, ans == Integer.MAX_VALUE? -1 : ans);

        return dp.get(target);
    }
}