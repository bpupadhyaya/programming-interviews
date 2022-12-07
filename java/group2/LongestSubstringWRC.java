// Find the length of the longest substring without repeating characters.
// Sample input: "xyzzxxyyzz", sample output: 3

import java.util.Map;
import java.util.HashMap;

class LongestSubstringWRC {
    public static void main(String[] args) {
        String input = "xyzzxxyyzza";
        System.out.println("Longest substring: " + findLongestSubstringWRC(input));
    }

    private static int findLongestSubstringWRC(String input) {
        int len = input.length();
        int result = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i =0, j = 0; i < len; i++) {
            if (map.containsKey(input.charAt(i))) {
                j = Math.max(map.get(input.charAt(i)), j);
            }
            result = Math.max(result, i - j + 1);
            map.put(input.charAt(i), i + 1);
        }
        return result;
    }
}