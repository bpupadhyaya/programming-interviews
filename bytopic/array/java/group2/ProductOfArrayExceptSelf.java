// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums
// except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.
// Example:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Tag: 13/150

import java.util.Arrays;
class ProductOfArrayExceptSelf {
    public static void main(String...args) {
        int[] data = {1,2,3,4};
        int[] result = productExceptSelf(data);
        System.out.println("Product: " + Arrays.toString(result));
    }

    static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i-1] * nums[i-1];
        }
        int right = 1;
        for (int i = n -1; i >=0; i--) {
            result[i] *= right;
            right *= nums[i];
        }
        return result;
    }
}

// Logic: