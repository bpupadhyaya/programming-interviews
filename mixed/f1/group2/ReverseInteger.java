// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
// to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
// Constraints: -2^(31) <= x <= 2^(31) - 1
// Sample 1: Input: 456, Output: 654

class ReverseInteger {
    public static void main(String...args) {
        int x = 456;
        System.out.println("Reverse: " + reverseInteger(x));
    }

    static int reverseInteger(int x) {
        long revNum = 0;
        while (x != 0) {
            int lastDig = x % 10;
            revNum += lastDig;
            revNum = revNum * 10;
            x = x / 10;
        }
        revNum = revNum / 10;
        if (revNum > Integer.MAX_VALUE || revNum < Integer.MIN_VALUE)
            return 0;
        if (x < 0)
            return (int) (-1 * revNum);

        return (int) revNum;
    }
}

// Soln: time complexity O(log(x))
// space complexity: O(1)