// A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
// For example, for arr = [1,2,3], the following are all the permutations of
// arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
// The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
// More formally, if all the permutations of the array are sorted in one container according to their
// lexicographical order, then the next permutation of that array is the permutation that follows it in the
// sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible
// order (i.e., sorted in ascending order).
// For example, the next permutation of arr = [1,2,3] is [1,3,2].
// Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
// While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical
// larger rearrangement. Given an array of integers nums, find the next permutation of nums.
// The replacement must be in place and use only constant extra memory.
// Sample 1:
// Input: nums = [1,2,3]
// Output: [1,3,2]

class NextPermutation {
    public static void main(String[] args) {
        int[] arr = {1,2,3};
        findNextPermutation(arr);
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + ", ");
        System.out.println();
    }

    static void findNextPermutation(int[] nums) {
        int pivot = indexOfLastPeak(nums) - 1;
        if (pivot != -1) {
            int nextPrefix = lastIndexOfGreater(nums, nums[pivot]);
            swap(nums, pivot, nextPrefix);
        }
        reverseSuffix(nums, pivot + 1);
    }

    static int indexOfLastPeak(int[] nums) {
        for (int i = nums.length - 1; 0 < i; --i) {
            if (nums[i-1] < nums[i])
                return i;
        }
        return 0;
    }

    static int lastIndexOfGreater(int[] nums, int threshold) {
        for (int i = nums.length - 1; 0 <= i; --i) {
            if (threshold < nums[i])
                return i;
        }
        return -1;
    }

    static void reverseSuffix(int[] nums, int start) {
        int end = nums.length - 1;
        while (start < end) {
            swap(nums, start++, end--);
        }
    }

    static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}