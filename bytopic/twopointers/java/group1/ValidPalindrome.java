// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric
// characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.
// Example:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
//
// Tag: 25/150
// Tag: 125/2927, R117/2936 (overall frequency ranking), fb R9/50

class ValidPalindrome {
    public static void main(String...args) {
        String s = "A man, a plan, a canal: Panama";
        System.out.println("Palindrome? " + isPalindrome(s));
    }

    static boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }
        int first = 0;
        int last = s.length() - 1;
        while (first <= last) {
            char currFirst = s.charAt(first);
            char currLast = s.charAt(last);
            if (!Character.isLetterOrDigit(currFirst)) {
                first++;
            } else if (!Character.isLetterOrDigit(currLast)) {
                last--;
            } else {
                if (Character.toLowerCase(currFirst) != Character.toLowerCase(currLast)) {
                    return false;
                }
                first++;
                last--;
            }
        }
        return true;
    }
}

// Complexity:
// Time complexity:
// The time complexity of this solution is O(n), where n is the length of the string. This is because, in the worst case,
// all characters in the string need to be checked once, so the number of operations is proportional to the length of the string.
// Space complexity:
// The space complexity of this solution is O(1), as no additional data structures are used, and only a constant amount of memory
// is required for the start and last pointers and a few variables.