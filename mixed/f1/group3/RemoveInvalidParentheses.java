// Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses
// to make the input string valid. Return a list of unique strings that are valid with the minimum number
// of removals. You may return the answer in any order.
// Sample 1:
// Input: s = "(x)())()"
//Output: ["(x())()","(x)()()"]
// Tag: fb R21/50

import java.util.List;
import java.util.ArrayList;

class RemoveInvalidParentheses {
    public static void main(String...args) {
        String myInput = "(x)())()";
        List<String> results = removeInvalidParentheses(myInput);
        for (String result: results) {
            System.out.println("Result: " + result);
        }

    }

    static List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<>();
        remove(s, result, 0, 0, new char[]{'(', ')'});
        return result;
    }

    private static void remove(String s, List<String> result, int last_i, int last_j, char[] par) {
        for (int stack = 0, i = last_i; i < s.length(); i++) {
            if (s.charAt(i) == par[0])
                stack++;
            if (s.charAt(i) == par[1])
                stack--;
            if (stack >= 0)
                continue;
            for (int j = last_j; j <= i; j++)
                if (s.charAt(j) == par[1] && (j == last_j || s.charAt(j - 1) != par[1]))
                    remove(s.substring(0, j) + s.substring(j + 1, s.length()), result, i, j, par);

            return;
        }
        String reversed = new StringBuilder(s).reverse().toString();
        if (par[0] == '(')
            remove(reversed, result, 0, 0, new char[]{')', '('});
        else
            result.add(reversed);
    }
}
