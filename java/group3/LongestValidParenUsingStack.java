// For a given character string containing only '(' and ')', find the length of the longest valid parentheses.
// Sample input: "()(()(", sample output: 2
// Soln: Time complexity: O(n), space complexity O(n)

import java.util.Stack;

class LongestValidParenUsingStack {
    public static void main(String... args) {
        String input = "()(())))))";
        System.out.println("Length of longest valid parentheses: " + longestValidParenStack(input));
    }

    private static int longestValidParenStack(String input) {
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    result = Math.max(result, i - stack.peek());
                }
            }
        }
        return result;
    }

}