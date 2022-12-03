// Given a string, find the length of longest non-repeating substring.

import java.util.Map;
import java.util.HashMap;

class LongestSubstring {
    public static void main(String[] args) {
        String myString = "xyzxyyzzxyza";
        System.out.println("Length of longest substring: "+findLongestSubstring(myString));
    }

    private static int findLongestSubstring(String myString) {
        int length = myString.length();
        int result = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0, j = 0; j < length; j++) {
            if (map.containsKey(myString.charAt(j))) {
                i = Math.max(i, map.get(myString.charAt(j)));
            }
            result = Math.max(result, j - i + 1);
            map.put(myString.charAt(j), j + 1);
        }
        return result;
    }
}