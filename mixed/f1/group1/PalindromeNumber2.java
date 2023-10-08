// Given an integer, return true if the integer is a palindrome, and false if otherwise.
// Sample 1:
// Input 242
// Output: true
// Sample 2:
// Input: -242
// Output: false, explanation: from lef it reads -242, from right it reads 242- and hence not a palindrome.
class PalindromeNumber2 {
    public static void main(String...args) {
        int myNumber = 242;
        System.out.println("Number: " + myNumber + " is palindrome (T/F): " + isPalindromeNumber(myNumber));
    }

    static boolean isPalindromeNumber(int x) {
        if (x < 0 || x != 0 && x % 10 == 0)
            return false;

        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x = x / 10;
        }

        return (x == rev || x == rev / 10);
    }
}