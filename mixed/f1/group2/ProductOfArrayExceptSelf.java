// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
// of nums except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.
// Sample 1:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]

import java.util.Arrays;
class ProductOfArrayExceptSelf {
    public static void main(String...args) {
        int nums[] = {1,2,3,4};
        int[] product = productExceptSelf(nums);
        for (int i = 0; i < product.length; i++) {
            System.out.print(product[i] + ",");
        }
        System.out.println();
    }

    static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int ans[] = new int[n];
        Arrays.fill(ans, 1);
        int curr = 1;
        for (int i = 0; i < n; i++) {
            ans[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;
        for (int i = n -1; i >= 0; i--) {
            ans[i] *= curr;
            curr *= nums[i];
        }
        return ans;
    }
}