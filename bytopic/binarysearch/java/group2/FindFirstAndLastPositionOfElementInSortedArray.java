// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
// of a given target value. If target is not found in the array, return [-1, -1].
// You must write an algorithm with O(log n) runtime complexity.
// Sxample 1:
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Soln: Time complexity: O(log(n)), space complexity: O(1)
//
// Tag: 118/150
// Tag: 34/2927, R114/2936 (overall frequency ranking)

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
        int[] result = {-1, -1};
        int left = binarySearch(nums, target, true);
        int right = binarySearch(nums, target, false);
        result[0] = left;
        result[1] = right;

        return result;
    }

    private static int binarySearch(int[] nums, int target, boolean isSearchingLeft) {
        int left = 0;
        int right = nums.length - 1;
        int index = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                index = mid;
                if (isSearchingLeft) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }

        return index;
    }
}