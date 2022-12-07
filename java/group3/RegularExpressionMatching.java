// Implement regular expression matching with support for '.' and '*'.
// '.' matches any single character, '*' matches zero or more of the preceding character.
// Sample input: string: "xxx", pattern: "x*", output: true
// Sample input: string: "xxx", pattern "x", output: false

class RegExpMatching {
    public static void main(String...args) {
        String input = "xxx";
        String pattern = "x*";
        System.out.println("Result: " +  isMatch(input, pattern));

    }

    private static boolean isMatch(String input, String pattern) {
        if (pattern.isEmpty())
            return input.isEmpty();
        boolean firstMatch = (!input.isEmpty() && (pattern.charAt(0) == input.charAt(0) ||
                pattern.charAt(0) == '.'));
        if (pattern.length() >= 2 && pattern.charAt(1) == '*') {
            return (isMatch(input, pattern.substring(2)) ||
                    (firstMatch && isMatch(input.substring(1), pattern)));
        } else {
            return firstMatch && isMatch(input.substring(1), pattern.substring(1));
        }
    }
}