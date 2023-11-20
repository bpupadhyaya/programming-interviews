// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.
// Example:
// Input: nums = [4,1,2,1,2]
// Output: 4
//
// Tag: 128/150
// Tag: 136/2927, R244/2936 (overall frequency ranking)

class SingleNumber {
    public static void main(String...args) {
        int[] nums = {4,1,2,1,2};
        System.out.println("Single number: " + singleNumber(nums));
    }

    static int singleNumber(int[] nums) {
        int ans = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ans = ans ^ nums[i];
        }

        return ans;
    }
}