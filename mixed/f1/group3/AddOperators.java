// Given a string num that contains only digits and an integer target, return all possibilities to insert
// the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression
// evaluates to the target value. Note that operands in the returned expressions should not contain leading zeros.
// Sample 1:
// Input: num = "232", target = 8
// Output: ["2*3+2","2+3*2"]
// Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

import java.util.List;
import java.util.ArrayList;
class AddOperators {
    public static void main(String...args) {
        String num = "232";
        int target = 8;
        List<String> expressions = findExpressions(num, target);
        System.out.println("Expressions: ");
        for (String expression: expressions) {
            System.out.println("Exp: " + expression);
        }

    }

    static List<String> findExpressions(String num, int target) {
        List<String> result = new ArrayList<String>();
        if (num == null || num.length() == 0)
            return result;
        helper(result, "", num, target, 0, 0, 0);

        return result;
    }

    static void helper(List<String> result, String path, String num, int target, int pos, long eval, long multed) {
        if (pos == num.length()) {
            if (target == eval)
                result.add(path);
            return;
        }
        for (int i = pos; i < num.length(); i++) {
            if (i != pos && num.charAt(pos) == '0')
                break;
            long cur = Long.parseLong(num.substring(pos, i + 1));
            if (pos == 0) {
                helper(result, path + cur, num, target, i + 1, cur, cur);
            } else {
                helper(result, path + "+" + cur, num, target, i + 1, eval + cur, cur);
                helper(result, path + "-" + cur, num, target, i + 1, eval - cur, -cur);
                helper(result, path + "*" + cur, num, target, i + 1, eval - multed + multed * cur, multed * cur);
            }
        }
    }
}


