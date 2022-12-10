// Convert a roman numeral to an integer.
// Time complexity: O(1), space complexity: O(1)

import java.util.Map;
import java.util.HashMap;

class RomanToInteger {
    public static void main(String[] args) {
        String myRoman = "DLV";
        System.out.println("Integer equivalent: " + convertRomanToInt(myRoman));
    }

    private static int convertRomanToInt(String roman) {
        Map<String, Integer> data = new HashMap<>();
        data.put("M", 1000);
        data.put("D", 500);
        data.put("C", 100);
        data.put("L", 50);
        data.put("X", 10);
        data.put("V", 5);
        data.put("I", 1);

        String lastSymbol = roman.substring(roman.length() - 1);
        int lastValue = data.get(lastSymbol);
        int total = lastValue;

        for (int i = roman.length() - 2; i >= 0; i--) {
            String currentSymbol = roman.substring(i, i+1);
            int currentValue = data.get(currentSymbol);
            if (currentValue < lastValue) {
                total -= currentValue;
            } else {
                total += currentValue;
            }
            lastValue = currentValue;
        }
        return total;
    }

}