// Convert a given integer to a roman numeral.
// Time complexity: O(1), space complexity: O(1)

class IntegerToRoman2 {
    public static void main(String...args) {
        int myNum = 555;
        //TODO bug fix needed.
        System.out.println("Equivalent roman: " + convertIntToRoman(myNum));
    }

    private static String convertIntToRoman(int myNum) {
        final String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        final int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1};

        StringBuilder s = new StringBuilder();
        for (int i = 0; i < values.length && myNum > 0; i++) {
            while (values[i] <= myNum) {
                myNum -= values[i];
                s.append(symbols[i]);
            }
        }
        return s.toString();
    }
}