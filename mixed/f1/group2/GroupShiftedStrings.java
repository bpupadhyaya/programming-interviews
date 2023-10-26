// We can shift a string by shifting each of its letters to its successive letter.
// For example, "abc" can be shifted to be "bcd".
// We can keep shifting the string to form a sequence.
// For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
// Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
// You may return the answer in any order.
// Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
// Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
class GroupShiftedString {
    public static void main(String...args) {
        String[] strings = {"abc","bcd","acef","xyz","az","ba","a","z"};
        List<List<String>> grStrings = groupStrings(strings);
        for (List<String> elem: grStrings)
            System.out.print(elem + ",");
        System.out.println();
    }

    static List<List<String>> groupStrings(String[] strings) {
        Map<String, List<String>> groupMap = new HashMap<>();
        for (String s: strings) {
            StringBuilder key = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                int relativeDistance = (s.charAt(i) - s.charAt(0) + 26) % 26;
                key.append(".");
                key.append(Integer.toString(relativeDistance));
            }
            String k = key.toString();
            if (!groupMap.containsKey(k)) {
                List<String> value = new ArrayList<>();
                groupMap.put(k, value);
            }
            groupMap.get(k).add(s);
        }
        System.out.println(groupMap);

        List<List<String>> output = new ArrayList<>();
        for (String key: groupMap.keySet()) {
            List<String> value = new ArrayList<>();
            value = groupMap.get(key);
            output.add(value);
        }

        return output;
    }
}