// Given two binary strings a and b, return their sum as a binary string.
// Sample 1:
// Input: a = "1010", b = "1011"
// Output: "10101"

class AddBinary {
    public static void main(String...args) {
        String a = "1010";
        String b = "1011";
        System.out.println("Sum: " + addBinary(a,b));
    }

    static String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            carry = sum > 1 ? 1 : 0;
            result.append(sum % 2);
        }
        if (carry != 0) result.append(carry);

        return result.reverse().toString();
    }
}