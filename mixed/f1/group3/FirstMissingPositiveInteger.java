// Given an unsorted integer array, return the smallest missing positive integer.
// Constraints: time complexity O(n) and O(1) of auxiliary space complexity
// Sample 1:
// Input: nums = [1,2,0]
// Output: 3
// Sample 2:
// Input nums = [4,5,6,8,9]
// Output: 1
// Sample 3:
// Input nums = [3,4,-1,1]
// Output: 2

class FirstMissingPositiveInteger {
    public static void main(String...args) {
        int[] nums = {1, 2, 0};
        System.out.println("First missing: " + findFirstMissingPositiveInteger(nums));
    }

    static int findFirstMissingPositiveInteger(int[] data) {
        // Apply cycle sort
        int i = 0;
        while (i < data.length) {
            int correct = data[i] - 1;
            if (data[i] <= data.length && data[i] > 0 && data[i] != data[correct]) {
                int temp = data[i];
                data[i] = data[correct];
                data[correct] = temp;
            } else {
                i++;
            }
        }

        int count = 0;
        // Once cycle sort is applied, find the first element that is not a the correct index
        // and return that index
        for (int j = 0; j < data.length; j++) {
            if (data[j] != j + 1) {
                return j + 1;
            }
        }
        // If every element is at its correct index, then the first missing
        // positive integer is data.length + 1
        return data.length + 1;
    }

}