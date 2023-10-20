// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
// of a given target value. If target is not found in the array, return [-1, -1].
// You must write an algorithm with O(log n) runtime complexity.
// Sxample 1:
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Soln: Time complexity: O(n), space complexity: O(1)

class FindFirstAndLastPositionOfElementInSortedArray {
    public static void main(String...args) {
        int[] nums = {5,7,7,8,8,10};
        int target = 8;
        int[] pos = findFirstAndLastPosition(nums, target);
        for (int i = 0; i < pos.length; i++)
            System.out.print(pos[i] + ", ");
        System.out.println();

    }

    static int[] findFirstAndLastPosition(int[] nums, int target) {
        int first = -1, last = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                if (first == -1) {
                    first = i;
                }
                last = i;
            }
        }
        return new int[]{first, last};
    }
}