// Detect if a given integer is a palindrome or not.
// Sample input: 12321 : palindrome, input: 12345 : not a palindrome, input -12321 : not a palindrome

class PalindromeNum1 {
    public static void main(String[] args){
        int inputNum = 12321;
        System.out.println("Result: " + isPalinNum1(inputNum));
    }

    private static boolean isPalinNum1(int num) {
        if (num < 0 || num % 10 == 0 && num != 0)
            return false;

        int revertedNum = 0;
        while (num > revertedNum) {
            revertedNum = revertedNum * 10 + num % 10;
            num /= 10;
        }

        return num == revertedNum || num == revertedNum / 10; // second condition takes care of odd length.
    }

}