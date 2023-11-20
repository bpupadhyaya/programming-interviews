// Given a string s which represents an expression, evaluate this expression and return its value.
// The integer division should truncate toward zero.
// You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^{31}, 2^{31} - 1].
// Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
// Sample 1:
// Input: s = " 3+5 / 2 "
// Output: 5
// Tag: fb R12/50

import java.util.Stack;
class BasicCalculatorII {
    public static void main(String...args) {
        String s = "3+5/2 ";
        System.out.println("Result: " + calculate(s));
    }

    static int calculate(String s) {
        int result = 0;
        if (s != null && s.length() > 0) {
            Stack<Integer> nums = new Stack();
            char lastOperator = '+';
            int num = 0;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (Character.isDigit(c)) {
                    num = num * 10 + c - '0';
                }
                if (isOperator(c) || i == s.length() - 1) {
                    if (lastOperator == '+') {
                        nums.push(num);
                    } else if (lastOperator == '-') {
                        nums.push(-1*num);
                    }
                    else if (lastOperator == '*') {
                        nums.push(nums.pop() * num);
                    } else if (lastOperator == '/') {
                        nums.push(nums.pop() / num);
                    }
                    num = 0;
                    lastOperator = c;
                }
            }
            while (!nums.isEmpty()) {
                result = result + nums.pop();
            }
        }
        return result;
    }

    private static boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }
}

// Constraints:
// 1 <= s.length <= 3 * 10^5
// s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
// s represents a valid expression.
// All the integers in the expression are non-negative integers in the range [0, 2^{31} - 1].
// The answer is guaranteed to fit in a 32-bit integer.