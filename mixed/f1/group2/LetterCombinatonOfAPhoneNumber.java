// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
// number could represent. Return the answer in any order.
// A mapping of digits to letters (just like on the telephone buttons) is given below.
// Note that 1 does not map to any letters.
// Mapping from phone pad:
// 1 (none), 2(abc), 3(def), 4(ghi), 5(jkl), 6(mno), 7(pqrs), 8(tuv), 9(wxyz)
// Sample 1:
// Input: digits = "23"
// Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
class LetterCombinationOfAPhoneNumber {
    public static void main(String...args) {
        String digits = "23";
        List<String> combinations = findCombinations(digits);
        System.out.println("Combination: ");
        for (String comb: combinations)
            System.out.print(comb + ",");
        System.out.println();


    }

    static List<String> findCombinations(String digits) {
        if (digits.isEmpty())
            return Collections.emptyList();

        String[] phone_map = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> output = new ArrayList<>();
        backtrack("", digits, phone_map, output);

        return output;
    }

    private static void backtrack(String combination, String next_digits, String[] phone_map, List<String> output) {
        if (next_digits.isEmpty()) {
            output.add(combination);
        } else {
            String letters = phone_map[next_digits.charAt(0) - '2'];
            for (char letter: letters.toCharArray()) {
                backtrack(combination + letter, next_digits.substring(1), phone_map, output);
            }
        }
    }
}
// Complexity:
// Time complexity: (O(4^n)), where (n) is the length of the input string. In the worst case,
// each digit can represent 4 letters, so there will be 4 recursive calls for each digit.
// Space complexity: (O(n)), where (n) is the length of the input string. This accounts for
// the recursion stack space.