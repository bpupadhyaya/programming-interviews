// Write an algorithm to determine if a number n is happy.
// A happy number is a number defined by the following process:
// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
// does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.
// Example:
// Input: n = 19
// Output: true
// Explanation:
// 1^2 + 9^2 = 82
// 8^2 + 2^2 = 68
// 6^2 + 8^2 = 100
// 1^2 + 0^2 + 0^2 = 1
//
// Tag: 45/150
// Tag: 202/2927, R157/2936 (overall frequency ranking)

import java.util.HashSet;
import java.util.Set;
class HappyNumber {
    public static void main(String[] args) {
        int n = 19;
        System.out.println("Is happy number? " + isHappy(n));
    }

    static boolean isHappy(int n) {
        // Create a set to keep track of the numbers that have already been seen.
        Set<Integer> seen = new HashSet<>();

        // Loop until either n becomes 1 (happy number) or n is seen again (not happy number).
        while (n != 1 && !seen.contains(n)) {
            // Add n to the set of seen numbers.
            seen.add(n);

            // Compute the sum of squares of the digits of n.
            int sum = 0;
            while (n != 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }

            // Update n with the sume of the squares of its digits.
            n = sum;
        }

        // If n is 1, it is a happy number; otherwise, it is not.
        return n ==1;
    }
}