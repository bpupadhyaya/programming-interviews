// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
// the integer. The digits are ordered from most significant to least significant in left-to-right order. The large
// integer does not contain any leading 0's.
// Increment the large integer by one and return the resulting array of digits.
// Example 1:
// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].
// Example 2:
// Input: digits = [9]
// Output: [1,0]
// Explanation: The array represents the integer 9.
// Incrementing by one gives 9 + 1 = 10.
// Thus, the result should be [1,0].
//
// Tag: 132/150
// Tag: 66/2927, R361/2936 (overall frequency ranking)

import java.util.Arrays;
class PlusOne {
    public static void main(String[] args) {
        int[] digits = {1,2,3};
        System.out.println("Plus one:  " + Arrays.toString(plusOne(digits)));
    }

    static int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        digits = new int[digits.length + 1];
        digits[0] = 1;

        return digits;
    }
}

// Complexity:
// TC ~ O(n)
// SC ~ O(n)