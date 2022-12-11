// Detect if a given string is a valid number or not.
// Rules:
// A sign character: '+' or '-'.
// One of the following items:
// One or more digits, followed by a dot '.'.
// One or more digits, followed by a dot '.', followed by one or more digits.
// A dot '.', followed by one or more digits.
// Sample valid numbers: ["7", "0012", "-0.2", "+3.14", "5.", "-.8", "3e10", "-80E3",
// "4e+7", "+7e-1", "45.5e95", "-103.486e769"],
// Sample invalid numbers: ["xyz", "3a", "e8", "78e2.6", "--7", "-+4", "84a64e45"].

import java.util.Map;
import java.util.Set;
import java.util.List;

class ValidNumber {
    public static void main(String[] args) {
        String myInput = "-103.486e769";
        String myInput2 = "abc.35";
        System.out.println("Result: " + isValid(myInput));
        // TODO needs a fix
        System.out.println("Result 2: " + isValid(myInput));
    }

    private static boolean isValid(String myInput) {
        final List<Map<String, Integer>> detFinAutomaton = List.of(
                Map.of("digit", 1, "sign", 2, "dot", 3),
                Map.of("digit", 1, "dot", 4, "exponent", 5),
                Map.of("digit", 1, "dot", 3),
                Map.of("digit", 4),
                Map.of("digit", 4, "exponent", 5),
                Map.of("sign", 6, "digit", 7),
                Map.of("digit", 7),
                Map.of("digit", 7)
        );

        final Set<Integer> validFinalStates = Set.of(1, 4, 7);

        int currentState = 0;
        String group = "";

        for (int i = 0; i < myInput.length(); i++) {
            char curr = myInput.charAt(i);
            if (Character.isDigit(curr)) {
                group = "digit";
            } else if (curr == '+' || curr == '-') {
                group = "sign";
            } else if (curr == 'e' || curr == 'E') {
                group = "exponent";
            } else if (curr == '.') {
                group = "dot";
            } else {
                return false;
            }

            if (!detFinAutomaton.get(currentState).containsKey(group)) {
                return false;
            }

            currentState = detFinAutomaton.get(currentState).get(group);
        }

        return validFinalStates.contains(currentState);
    }

}


