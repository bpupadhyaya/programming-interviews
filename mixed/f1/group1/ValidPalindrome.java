// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
// removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
// characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.
// Sample 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

class ValidPalindrome {
    public static void main(String...args) {
        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));
    }

    static boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }

        int start = 0;
        int last = s.length() - 1;
        while (start <= last) {
            char currFirst = s.charAt(start);
            char currLast = s.charAt(last);
            if (!Character.isLetterOrDigit(currFirst)) {
                start++;
            } else if (!Character.isLetterOrDigit(currLast)) {
                last--;
            } else {
                if (Character.toLowerCase(currFirst) != Character.toLowerCase(currLast)) {
                    return false;
                }
                start++;
                last--;
            }
        }
        return true;
    }
}