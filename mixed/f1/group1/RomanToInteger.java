// Given a roman numeral, convert it to an integer.
// (Symbol, Value): (I, 1), (V, 5), (X, 10), (L, 50), (C, 100), (D, 500), (M, 1000)
// Sample 1:
// Input: s = "MCMXCIV"
// Output: 1994
class RomanToInteger {
    public static void main(String...args) {
        String roman = "MCMXCIV";
        System.out.println("Integer equivalent: " + romanToInteger(roman));
    }

    static int romanToInteger(String roman) {
        int result = 0, num = 0;
        for (int i = roman.length() - 1; i >=0; i--) {
            switch(roman.charAt(i)) {
                case 'I': num = 1; break;
                case 'V': num = 5; break;
                case 'X': num = 10; break;
                case 'L': num = 50; break;
                case 'C': num = 100; break;
                case 'D': num = 500; break;
                case 'M': num = 1000; break;
            }
            if (4 * num < result)
                result -= num;
            else
                result += num;
        }
        return result;
    }
}