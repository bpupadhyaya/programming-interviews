// Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
// whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
// Example:
// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.
//
// Tag: 30/150
// Tag: 209/2927, R394/2936 (overall frequency ranking)

class MinimumSizeSubArraySum {
    public static void main(String...args) {
        int[] nums = {2,3,1,2,4,3};
        int target = 7;
        System.out.println("Min Subarray length: " + minSubArrayLen(target, nums));
    }

    static int minSubArrayLen(int target, int[] nums) {
        int i = 0, j = 0, sum = 0;
        int min = Integer.MAX_VALUE;
        while (j < nums.length) {
            sum += nums[j];
            while (sum >= target) {
                sum -= nums[i];
                min = Math.min(j-i+1, min);
                i++;
            }
            j++;
        }
        if (min == Integer.MAX_VALUE)
            return 0;

        return min;
    }
}

// Steps:
// 1. Initialize two pointers, i and j, to track the start and end of the current subarray, respectively. Set i and j to 0 initially.
// 2. Initialize a variable sum to keep track of the current sum of elements in the subarray.
// 3. Initialize a variable mn to store the minimum length found so far. Set it to the maximum possible integer value (INT_MAX).
// 4. Start a while loop that continues until the j pointer reaches the end of the array nums.
// 5. Inside the loop, add the element at index j to the sum variable.
// 6. Check if the sum is greater than or equal to the target value.
// 7. If the condition is true, enter another while loop. This loop will handle the case where the current subarray sum is equal to or
// greater than the target.
//  a. Decrement the sum by subtracting the element at index i.
//  b. Update mn with the minimum length found so far (j - i + 1).
//  c. Increment the i pointer to move the window to the right.
//  d. Repeat steps a-c until the sum is no longer greater than or equal to the target value.
// 8. Increment the j pointer to move the window to the right.
// 9. Repeat steps 5-8 until the j pointer reaches the end of the array.
// 10. After the loop, check if the value of mn is still INT_MAX, indicating that no subarray was found. In this case, return 0.
// 11. Otherwise, return the value of mn, which represents the minimum length of a subarray whose sum is greater than or equal to the target.
//
// The sliding window technique allows us to efficiently search for the minimum length subarray that satisfies the given condition.
// By maintaining two pointers and adjusting the window based on the sum of elements, we can avoid unnecessary computations and achieve
// a time complexity of O(N), where N is the size of the input array nums.
//
// Complexity
// Time complexity ~ O(n)
// Space complexity ~ O(1)