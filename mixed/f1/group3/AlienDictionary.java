// There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
// You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings
// in words are sorted lexicographically by the rules of this new language. If this claim is incorrect, and the
// given arrangement of string in words cannot correspond to any order of letters, return "".
// Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing
// order by the new language's rules. If there are multiple solutions, return any of them.
// Sample 1:
// Input: words = ["wrt","wrf","er","ett","rftt"]
// Output: "wertf"

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
class AlienDictionary {
    public static void main(String...args) {
        String[] words = {"wrt","wrf","er","ett","rftt"};
        System.out.println("Result: " + findUniqueLettersAsc(words));
    }

    static String findUniqueLettersAsc(String[] words) {
        Map<Character, Set<Character>> map = new HashMap<Character, Set<Character>>();
        Map<Character, Integer> degree = new HashMap<Character, Integer>();
        String result = "";
        if (words == null || words.length == 0) return result;
        for (String s: words) {
            for (char c: s.toCharArray()) {
                degree.put(c, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String cur = words[i];
            String next = words[i+1];
            int length = Math.min(cur.length(), next.length());
            for(int j = 0; j < length; j++) {
                char c1 = cur.charAt(j);
                char c2 = next.charAt(j);
                if (c1 != c2) {
                    Set<Character> set = new HashSet<Character>();
                    if (map.containsKey(c1))
                        set = map.get(c1);
                    if(!set.contains(c2)) {
                        set.add(c2);
                        map.put(c1, set);
                        degree.put(c2, degree.get(c2)+1);
                    }
                    break;
                }
            }
        }

        Queue<Character> q = new LinkedList<Character>();
        for(char c: degree.keySet()) {
            if (degree.get(c) == 0)
                q.add(c);
        }
        while (!q.isEmpty()) {
            char c = q.remove();
            result += c;
            if(map.containsKey(c)) {
                for (char c2: map.get(c)) {
                    degree.put(c2, degree.get(c2) - 1);
                    if (degree.get(c2) == 0)
                        q.add(c2);
                }
            }
        }
        if (result.length() != degree.size())
            return "";

        return result;
    }
}
