// Given a string, return if the string is a valid number.
// Example of valid numbers:
// ["5", "0078", "-0.6", "+3.14", "7.", "-.9", "2e10", "-80E3", "5e+7",
// "+7e-1", "75.5e93", "-564.456e789"]


class ValidNumber {
    public static void main(String...args) {
        String stringNumber = "-564.456e789";
        System.out.println("Is valid number? " + isValidNumber(stringNumber));
    }

    static boolean isValidNumber(String s) {
        s = s.trim();
        boolean dotSeen = false;
        boolean eSeen = false;
        boolean numberSeen = false;
        boolean numberAfterE = true;

        for (int i = 0; i < s.length(); i++) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                numberSeen = true;
                numberAfterE = true;
            } else if (s.charAt(i) == '.') {
                if (eSeen || dotSeen) {
                    return false;
                }
                dotSeen = true;
            } else if (s.charAt(i) == 'e') {
                if (eSeen || !numberSeen) {
                    return false;
                }
                numberAfterE = false;
                eSeen = true;
            } else if (s.charAt(i) == '-' || s.charAt(i) == '+') {
                if (i != 0 && s.charAt(i - 1) != 'e') {
                    return false;
                }
            } else {
                return false;
            }
        }

        return numberSeen && numberAfterE;
    }
}

// Soln: Valid number matches regex: [-+]?(([0-9]+(.[0-9]*)?)|.[0-9]+)(e[-+]?[0-9]+)?

