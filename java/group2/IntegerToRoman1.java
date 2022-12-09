// Convert a given integer to a roman numeral.
// Time complexity: O(1), space complexity: O(1)

class IntegerToRoman1 {
    public static void main(String[] args) {
        int myInput = 555;
        System.out.println("Equivalent roman: " + convertIntToRoman(myInput));
    }

    private static String convertIntToRoman(int input) {
        final String[] thousands = {"", "M", "MM", "MMM"};
        final String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        final String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        final String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        return thousands[input / 1000] + hundreds[input % 1000 / 100] + tens[input % 100 / 10] + ones[input % 10];
    }
}