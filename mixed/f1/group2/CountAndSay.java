// The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
// countAndSay(1) = "1"
// countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then
// converted into a different digit string.
// To determine how you "say" a digit string, split it into the minimal number of substrings such that each
// substring contains exactly one unique digit. Then for each substring, say the number of digits, then say
// the digit. Finally, concatenate every said digit.
// Input: n = 4
// Output: "1211"
// Explanation:
// countAndSay(1) = "1"
// countAndSay(2) = say "1" = one 1 = "11"
// countAndSay(3) = say "11" = two 1's = "21"
// countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
// Note: debug the program and check if answer is right.

class CountAndSay {
    public static void main(String...args) {
        int n = 4;
        System.out.println("Count and say: " + countAndSay(n));
    }

    static String countAndSay(int n) {
        String s = "1";
        for (int i = 0; i < n; i++) {
            s = countIdx(s);
        }
        return s;
    }

    private static String countIdx(String s) {
        StringBuilder sb = new StringBuilder();
        char c = s.charAt(0);
        int count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                count++;
            } else {
                sb.append(count);
                sb.append(c);
                c = s.charAt(i);
                count = 1;
            }
        }
        sb.append(count);
        sb.append(c);
        return sb.toString();
    }
}