// Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
// The returned integer should be non-negative as well.
// You must not use any built-in exponent function or operator.
// For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
// Example:
// Input: x = 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
//
// Tag: 134/150
// Tag: 69/2927, R187/2936 (overall frequency ranking)

class Sqrtx {
    public static void main(String...args) {
        int x = 8;
        System.out.println("Sqrt: " + mySqrt(x));
    }

    static int mySqrt(int x) {
        long r = x;
        while (r * r > x)
            r = (r + x / r) / 2;

        return (int)r;
    }
}