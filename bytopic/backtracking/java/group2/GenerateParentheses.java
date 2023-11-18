// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
// Example:
// Input: n = 3
// Output: ["((()))","(()())","(())()","()(())","()()()"]
// Input: n = 1
// Output: ["()"]
//
// Tag: 106/150
// Tag: 22/2927, R32/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
class ParenthesesGeneration {
    public static void main(String...args) {
        int n = 3;
        System.out.println("Result: " + generateParentheses(n));
    }

    static List<String> generateParentheses(int n) {
        List<String> result = new ArrayList<String>();
        recurse(result, 0, 0, "", n);
        return  result;
    }

    static void recurse(List<String> result, int left, int right, String s, int n) {
        if (s.length() == n * 2) {
            result.add(s);
            return;
        }

        if (left < n) {
            recurse(result, left+1, right, s + "(", n);
        }
        if (right < left) {
            recurse(result, left, right+1, s + ")", n);
        }
    }
}
// Steps:
// - The idea is to add ')' only after valid '('
// - We use two integer variables left & right to see how many '(' & ')' are in the current string
// - If left < n then we can add '(' to the current string
// - If right < left then we can add ')' to the current string
//
// Recursion tree for n = 2:
// 								   	(0, 0, '')
//								 	    |
//									(1, 0, '(')
//								   /           \
//							(2, 0, '((')      (1, 1, '()')
//							   /                 \
//						(2, 1, '(()')           (2, 1, '()(')
//						   /                       \
//					(2, 2, '(())')                (2, 2, '()()')
//						      |	                             |
//					res.append('(())')             res.append('()()')