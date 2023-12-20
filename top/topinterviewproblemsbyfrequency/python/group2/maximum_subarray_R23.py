"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Tag: Tag: R23/145
"""


def max_sub_array(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(nums))


if __name__ == "__main__":
    main()


"""
Intuition
The Intuition behind the code is to find the maximum sum of a contiguous subarray within the given array nums. 
It does this by scanning through the array and keeping track of the current sum of the subarray. Whenever the 
current sum becomes greater than the maximum sum encountered so far, it updates the maximum sum. If the current 
sum becomes negative, it resets the sum to 0 and starts a new subarray. By the end of the loop, the code returns 
the maximum sum found.

Approach:
We start by initializing two variables: maxSum and currentSum.
maxSum represents the maximum sum encountered so far and is initially set to the minimum possible integer value 
to ensure that any valid subarray sum will be greater than it.
currentSum represents the current sum of the subarray being considered and is initially set to 0.
We iterate through the nums array using a for loop, starting from the first element and going up to the last element.
For each element in the array, we add it to the current sum currentSum. This calculates the sum of the subarray 
ending at the current element.
Next, we check if the current sum currentSum is greater than the current maximum sum maxSum.
If it is, we update maxSum with the new value of currentSum. This means we have found a new maximum subarray sum.
If the current sum currentSum becomes negative, it indicates that including the current element in the subarray 
would reduce the overall sum. In such cases, we reset currentSum to 0. This effectively discards the current 
subarray and allows us to start a fresh subarray from the next element.
We repeat steps 3 to 5 for each element in the array.
After iterating through the entire array, the variable maxSum will contain the maximum subarray sum encountered.
Finally, we return the value of maxSum as the result, representing the maximum sum of a contiguous subarray within 
the given array nums.
"""
