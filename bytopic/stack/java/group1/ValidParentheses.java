// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
// is valid. An input string is valid if:
// 1. Open brackets must be closed by the same type of brackets.
// 2. Open brackets must be closed in the correct order.
// 3. Every close bracket has a corresponding open bracket of the same type.
// Example 1:
// Input: s = "()[]{}"
// Output: true
// Example 2:
// Input: s = "(]"
// Output: false
// Tag: 52/150
// Tag: 20/2927

import java.util.Stack;
class ValidParentheses {
    public static void main(String[] args) {
        String s = "()[]{}";
        System.out.println("Is valid? " + isValid(s));
    }

    static boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c: s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) { // No matching opening bracket
                    return false;
                }

                char top = stack.peek();
                if ((c == ')' && top == '(') || (c == ']' && top == '[') || (c == '}' && top == '{')) {
                    stack.pop();
                } else { // Brackets don't match
                    return false;
                }
            }
        }

        return stack.isEmpty(); // Should be empty in order to match
    }
}