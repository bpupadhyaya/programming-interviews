// For a given character string containing only '(' and ')', find the length of the longest valid parentheses.
// Sample input: "()(()(", sample output: 2
// Soln: Time complexity: O(n), space complexity O(1)

class LongestValidParen {
    public static void main(String...args) {
        String input = "()(()((())";
        System.out.println("Length of longest valid parentheses: " + longestValidParen(input));
    }

    private static int longestValidParen(String input) {
        int left = 0;
        int right = 0;
        int maxLength = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '('){
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * right);
            } else if (right >= left) {
                left = 0;
                right = 0;
            }
        }
        left = right = 0;
        for (int i = input.length() - 1; i >= 0; i--) {
            if (input.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * left);
            } else if (left >= right) {
                left = 0;
                right = 0;
            }
        }
        return maxLength;
    }

}