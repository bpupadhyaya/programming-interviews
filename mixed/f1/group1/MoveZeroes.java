// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
// Note that you must do this in-place without making a copy of the array.
// Sample 1:
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]

class MoveZeroes {
    public static void main(String...args) {
        int[] nums = {0,1,0,3,12};
        moveZeroes(nums);
        for (int i = 0; i < nums.length; i++)
            System.out.print(nums[i] + ",");
        System.out.println();
    }

    static void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0)
            return;
        int insertPos = 0;
        for (int num: nums) {
            if (num != 0)
                nums[insertPos++] = num;
        }

        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }
}