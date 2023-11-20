// Given an integer n, return the number of trailing zeroes in n!.
// Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
// Example 1:
// Input: n = 5
// Output: 1
// Explanation: 5! = 120, one trailing zero.
// Example 2:
// Input: n = 3
// Output: 0
// Explanation: 3! = 6, no trailing zero.
//
// Tag: 133/150
// Tag: 172/2927, R1049/2936 (overall frequency ranking)

class FactorialTrailingZeroes {
    public static void main(String[] args) {
        int n = 5;
        System.out.println("Trailing zeroes: " + trailingZeroes(n));
    }

    static int trailingZeroes(int n) {
        int r = 0;
        while (n > 0) {
            n /= 5;
            r += n;
        }

        return r;
    }
}