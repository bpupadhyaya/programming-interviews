// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
// typically using all the original letters exactly once.
// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:
// Input: s = "rat", t = "car"
// Output: false
// Tag: 42/150

import java.util.HashMap;
import java.util.Map;
class ValidAnagram1 {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println("Valid anagram? " + isAnagram(s, t));
    }

    static boolean isAnagram(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();

        // Count the frequency of characters in string s.
        for (char x: s.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        // Decrement the frequency of characters using string t.
        for (char x: t.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) - 1);
        }

        // Check if any character has non-zero frequency
        for (int val: count.values()) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
}