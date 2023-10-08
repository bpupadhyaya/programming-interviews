// Given an integer, return true if the integer is a palindrome, and false if otherwise.
// Sample 1:
// Input 242
// Output: true
// Sample 2:
// Input: -242
// Output: false, explanation: from lef it reads -242, from right it reads 242- and hence not a palindrome.
class PalindromeNumber1 {
    public static void main(String...args) {
        int myNumber = 242;
        System.out.println("Number: " + myNumber + " is palindrome (T/F): " + isPalindromeNumber(myNumber));
    }

    static boolean isPalindromeNumber(int x) {
        String s = String.valueOf(x);
        int n = s.length();

        for(int i=0; i<n/2; i++) {
            if (s.charAt(i) != s.charAt(n-i-1))
                return false;
        }
        return true;
    }
}