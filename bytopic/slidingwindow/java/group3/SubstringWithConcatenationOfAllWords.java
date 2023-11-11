// You are given a string s and an array of strings words. All the strings of words are of the same length.
// A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
// For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
// all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any
// permutation of words.
// Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
// Input: s = "barfoothefoobarman", words = ["foo","bar"]
// Output: [0,9]
// Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
// The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
// The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
// The output order does not matter. Returning [9,0] is fine too.
// Tag: 32/150

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
class SubstringWithConcatenationOfAllWords {
    public static void main(String[] args) {
        String s = "barfoothefoobarman";
        String[] words = {"foo","bar"};
        System.out.println("Substring indices: " + findSubstring(s, words));
    }

    static List<Integer> findSubstring(String s, String[] words) {
        final Map<String, Integer> counts = new HashMap<>();
        for (final String word: words) {
            counts.put(word, counts.getOrDefault(word, 0) +1);
        }
        final List<Integer> indices = new ArrayList<>();
        final int n = s.length(), num = words.length, len = words[0].length();
        for (int i = 0; i < n - num * len + 1; i++) {
            final Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < num) {
                final String word = s.substring(i+j*len, i+(j+1)*len);
                if (counts.containsKey(word)) {
                    seen.put(word, seen.getOrDefault(word, 0) +1);
                    if (seen.get(word) > counts.getOrDefault(word, 0)) {
                        break;
                    }
                } else {
                    break;
                }
                j++;
            }
            if (j == num) {
                indices.add(i);
            }
        }
        return indices;
    }
}
