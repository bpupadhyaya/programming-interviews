// Given an integer, return true if the integer is a palindrome, and false if otherwise.
// Sample 1:
// Input 242
// Output: true
// Sample 2:
// Input: -242
// Output: false, explanation: from lef it reads -242, from right it reads 242- and hence not a palindrome.

class PalindromeNumber {
    public static void main(String...args) {
        int myNumber = 242;
        System.out.println("Number: " + myNumber + " is palindrome (T/F): " + isPalindromeNumber(myNumber));
    }

    static boolean isPalindromeNumber(int x) {
        StringBuilder s = new StringBuilder(String.valueOf(x));
        s.reverse();

        return s.toString().equals(x + "");
    }
}