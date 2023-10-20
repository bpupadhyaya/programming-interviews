// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.
// An input string is valid if:
// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
// Sample 1:
// Input: s = "()[]{}"
// Output: true

import java.util.Stack;
class ValidParentheses {
    public static void main(String...args) {
        String exp = "()[]{}";
        System.out.println("Valid? " + isValidParentheses(exp));
    }

    static boolean isValidParentheses(String exp) {
        Stack<Character> stack = new Stack<Character>();
        for (char c: exp.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }
}