// Detect if a given integer is a palindrome or not.
// Sample input: 12321 : palindrome, input: 12345 : not a palindrome, input -12321 : not a palindrome

class PalindromeNum {
    public static void main(String[] args){
        int inputNum = 1111;
        System.out.println("Result: " + isPalinNum(inputNum));
    }

    private static boolean isPalinNum(int inputNum) {
        String input = inputNum+"";
        int len = input.length();
        boolean palin = true;
        for (int i = 0; i < len / 2; i++) {
            if (input.charAt(i) != input.charAt(len - i -1 ))
                palin = false;
            else
                continue;
        }
        return palin;
    }
}