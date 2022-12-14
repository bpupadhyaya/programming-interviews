// Rotate a given array to the right by k steps, where k is non-negative.
// Sample input: Input: [5,15,25,35,45,55,65], k = 2
// Sample output: [55,65,5,15,25,35,45]
// Solution: time complexity: O(n), space complexity: O(1)

class RotateArray {
    public static void main(String[] args) {
        int[] myArray = {5,15,25,35,45,55,65};
        int k = 2;
        rotateArray(myArray, k);
        for (int i = 0; i < myArray.length; i++) {

            System.out.print("," + myArray[i]);
        }
        System.out.println();
    }

    private static void rotateArray(int[] myArray, int k) {
        k %= myArray.length;
        reverse(myArray, 0, myArray.length - 1);
        reverse(myArray, 0, k - 1);
        reverse(myArray, k, myArray.length - 1);
    }
    private static void reverse(int[] myArray, int start, int end) {
        while (start < end) {
            int temp = myArray[start];
            myArray[start] = myArray[end];
            myArray[end] = temp;
            start++;
            end--;
        }
    }

}