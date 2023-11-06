// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
// elements may be changed. Then return the number of elements in nums which are not equal to val.
// Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
// following things:
// Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
// The remaining elements of nums are not important as well as the size of nums.
// Return k.
// Example:
// Input: nums = [0,1,2,2,3,0,4,2], val = 2
// Output: 5, nums = [0,1,4,0,3,_,_,_]
// Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
// Note that the five elements can be returned in any order.
// It does not matter what you leave beyond the returned k (hence they are underscores).
// Tag: 2/150

class ElementRemoval {
    public static void main(String[] args) {
        int[] nums = {0,1,2,2,3,0,4,2};
        int target = 2;
        System.out.println("Num of elements: " + removeElement(nums,target));

    }

    static int removeElement(int[] nums, int val) {
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}

// Intuition:
// The intuition behind this solution is to iterate through the array and keep track of two pointers: index and i.
// The index pointer represents the position where the next non-target element should be placed, while the i pointer
// iterates through the array elements. By overwriting the target elements with non-target elements, the solution
// effectively removes all occurrences of the target value from the array.
// Approach:
// 1. Initialize index to 0, which represents the current position for the next non-target element.
// 2. Iterate through each element of the input array using the i pointer.
// 3. For each element nums[i], check if it is equal to the target value.
//      -If nums[i] is not equal to val, it means it is a non-target element.
//      -Set nums[index] to nums[i] to store the non-target element at the current index position.
//      -Increment index by 1 to move to the next position for the next non-target element.
// 4. Continue this process until all elements in the array have been processed.
// 5. Finally, return the value of index, which represents the length of the modified array.
// Complexity:
// Time complexity:
// O(n)
// Space complexity:
// O(1)