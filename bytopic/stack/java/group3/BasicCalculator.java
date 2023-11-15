// Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return
// the result of the evaluation.
// Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
// such as eval().
// Example:
// Input: s = "(1+(4+5+2)-3)+(6+8)"
// Output: 23
//
// Tag: 56/150
// Tag: 224/2927, R252/2936 (overall frequency ranking)

import java.util.Stack;
class BasicCalculator {
    public static void main(String...args) {
        String s = "(1+(4+5+2)-3)+(6+8)";
        System.out.println("Reuslt: " + calculate(s));
    }

    static int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        int result = 0;
        int number = 0;
        int sign = 1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                number = 10 * number + (int)(c - '0');
            } else if (c == '+') {
                result += sign * number;
                number = 0;
                sign = 1;
            }else if (c == '-') {
               result += sign * number;
               number = 0;
               sign = -1;
            } else if (c == '(') {
                // We push the result first, then sign.
                stack.push(result);
                stack.push(sign);
                // Reset the sign and result for the value in the parenthesis
                sign = 1;
                result = 0;
            } else if (c == ')') {
                result += sign * number;
                number = 0;
                result *= stack.pop(); // This pop is the sign before the parenthesis
                result += stack.pop(); // This is the result calculated before the parenthesis
            }
        }

        if (number != 0)
            result += sign * number;
        return result;
    }
}