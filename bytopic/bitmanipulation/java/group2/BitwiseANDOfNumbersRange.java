// Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers
// in this range, inclusive.
// Example:
// Input: left = 5, right = 7
// Output: 4
//
// Tag: 130/150
// Tag: 201/2927, R2106/2936 (overall frequency ranking)

class BitwiseANDOfNumbersRange {
    public static void main(String[] args) {
        int left = 5;
        int right = 7;
        System.out.println("Range bitwise AND result: " + rangeBitwiseAnd(left, right));
    }

    static int rangeBitwiseAnd(int left, int right) {
        while (right > left)
            right = right & right - 1;

        return left & right;
    }
}

// Idea ansd steps:
// Bitwise-AND of any two numbers will always produce a number less than or equal to the smaller number.
//
// Consider the following example:
//
//									12 ---- 1100
//									11 ---- 1011
//									10 ---- 1010
//									9  ---- 1001
//									8  ---- 1000
//									7  ---- 0111
//									6  ---- 0110
//									5  ---- 0101
//
// Desired Range: [5,12]
// Starting from 12, the loop will first do
// 12 & 11 = 8
// Next iteration, the loop will do
// 8 & 7 = 0
// why did we skip ANDing of 10,9? Because even if we did so, the result would eventually be anded with 8 whose value
// would be lesser than equal to 8.
// Hence, you start from the range end and keep working your way down the range till you reach the start.