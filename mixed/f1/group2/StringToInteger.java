// Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
// (similar to C/C++'s atoi function).
// The algorithm for myAtoi(string s) is as follows:
// 1. Read in and ignore any leading whitespace.
// 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character
// in if it is either. This determines if the final result is negative or positive respectively. Assume the result
// is positive if neither is present.
// 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of
// the string is ignored.
// 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the
// integer is 0. Change the sign as necessary (from step 2).
// 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it
// remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater
// than 231 - 1 should be clamped to 231 - 1.
// 6. Return the integer as the final result.
// Note:
// Only the space character ' ' is considered a whitespace character.
// Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
// Sample 1:
// Input: s = "42"
// Output: 42

class StringToInteger {
    public static void main(String...args) {
        String s = "42";
        System.out.println("Integer equivalent: " + myAtoi(s));
    }

    static int myAtoi(String s) {
        final int len = s.length();
        if (len == 0)
            return 0;

        int index = 0;
        while (index < len && s.charAt(index) == ' ') {
            index++;
        }

        if (index == len) {
            return 0;
        }

        char ch;
        boolean isNegative = (ch = s.charAt(index)) == '-';

        if (isNegative || ch == '+')
            index++;

        final int maxLimit = Integer.MAX_VALUE / 10;
        int result  = 0;
        while (index < len && isDigit(ch = s.charAt(index))) {
            int digit = ch - '0';
            if (result > maxLimit || (result == maxLimit && digit > 7)) {
                return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            result = (result * 10) + digit;
            index++;
        }

        return isNegative ? -result : result;
    }

    private static boolean isDigit(char ch) {
        return ch >= '0' && ch <= '9';
    }
}