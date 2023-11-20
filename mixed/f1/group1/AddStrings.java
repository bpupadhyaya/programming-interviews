// Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
// You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
// You must also not convert the inputs to integers directly.
// Constraints:
// 1 <= num1.length, num2.length <= 10^4
// num1 and num2 consist of only digits.
// num1 and num2 don't have any leading zeros except for the zero itself.
// Sample 1:
// Input: num1 = "11", num2 = "123"
// Output: "134"
// Tag: fb R31/50

class AddStrings {
    public static void main(String...args) {
        String num1 = "11";
        String num2 = "123";
        System.out.println("Sum " + addStrings(num1, num2));
    }

    static String addStrings(String num1, String num2) {
        int carry = 0;
        StringBuilder result = new StringBuilder();
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        while (i >= 0 || j >=0 ) {
            int n1 = (i < 0)? 0 : num1.charAt(i) - '0';
            int n2 = (j < 0)? 0 : num2.charAt(j) - '0';

            int sum = n1 + n2 + carry;
            result.append(sum % 10);
            carry = sum / 10;

            i--;
            j--;
        }
        if (carry == 1)
            result.append(carry);

        return result.reverse().toString();
    }
}
