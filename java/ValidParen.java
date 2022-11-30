import java.util.Stack;
import java.util.HashMap;

class ValidParen {
    public static void main(String...args) {
        HashMap<Character, Character> mappings;
        mappings = new HashMap<>();
        mappings.put(')', '(');
        mappings.put('}', '{');
        mappings.put(']', '[');

        String myExpr1 = "()()";
        boolean result1 = isValid(mappings, myExpr1);
        System.out.println(result1);

        String myExpr2 = "([)]";
        boolean result2 = isValid(mappings, myExpr2);
        System.out.println(result2);
    }

    private static boolean isValid(HashMap<Character, Character> mappings, String expr) {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i < expr.length(); i++) {
            char currChar = expr.charAt(i);
            if(mappings.containsKey(currChar)) {
              char topElement = stack.empty() ? '#' : stack.pop();
              if(topElement != mappings.get(currChar)) {
                  return false;
              }
            } else {
                stack.push(currChar);
            }
        } return stack.isEmpty();
    }

}