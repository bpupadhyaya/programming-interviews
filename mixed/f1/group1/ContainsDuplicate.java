// Given an integer array nums, return true if any value appears at least twice in the array, and return false if
// every element is distinct.
// Sample 1:
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

class ContainsDuplicate {
    public static void main(String[] args) {
        int[] nums = {1,1,1,3,3,4,3,2,4,2};
        System.out.println("Contains duplicate? " + containsDuplicate(nums));
    }

    static boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j])
                    return true;
            }
        }

        return false;
    }
}