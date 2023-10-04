// Given a string, find the length of the longest substring without repeating characters.
// Constraints: 0 <= string.length <= (5 *(10^4))
// Sample input: xyzxyzxy
// Sample output: 3
// Soln: Time complexity O(n)
// Space complexity: O(k), where k is the number of distinct charaters present in the hashset

import java.util.Set;
import java.util.HashSet;
class LongestSubstringWRC {
    public static void main(String...args) {
        String givenString = "xyzmnxyzxy";
        System.out.println("Longest substring length: "+findLongestSubstringLength(givenString));
    }

    static int findLongestSubstringLength(String s) {
        Set<Character> mySet = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        for(int right = 0; right < s.length(); right++) {
            if(!mySet.contains(s.charAt(right))) {
                mySet.add(s.charAt(right));
                maxLength = Math.max(maxLength, right-left+1);
            } else {
                while(s.charAt(left) != s.charAt(right)) {
                    mySet.remove(s.charAt(left));
                    left++;
                }
                mySet.remove(s.charAt(left));
                left++;
                mySet.add(s.charAt(right));
            }
        }

        return maxLength;
    }
}