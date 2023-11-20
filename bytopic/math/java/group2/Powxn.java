// Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
// Sample 1:
// Input: x = 2.00000, n = -2
// Output: 0.25000
//
// Tag: 135/150
// Tag: 50/2927, R98/2936 (overall frequency ranking), fb R5/50

class Powxn {
    public static void main(String...args) {
        double x = 2.0;
        int n = -2;
        System.out.println("Pow(x,n): " + myPow(x, n));
    }

    static double myPow(double x, int n) {
        if (n < 0) {
            n = -n;
            x = 1 / x;
        }
        double pow = 1;
        while (n != 0) {
            if ((n & 1) != 0) {
                pow *= x;
            }

            x *= x;
            n >>>= 1;
        }
        return pow;
    }
}