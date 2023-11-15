// You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
// Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are
// at nums[i], you can jump to any nums[i + j] where:
// 0 <= j <= nums[i] and
// i + j < n
// Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach
// nums[n - 1].
// Example:
// Input: nums = [2,3,1,1,4]
//Output: 2
//Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
// then 3 steps to the last index.
//
// Tag: 10/150
// Tag: 45/2927, R258/2936 (overall frequency ranking)

class JumpGameII2 {
    public static void main(String[] args) {
        int[] nums = {2,3,1,1,4};
        System.out.println("Min. number of jumps: " + jump(nums));
    }

    static int jump(int[] nums) {
        int ans = 0;
        int end = 0;
        int farthest = 0;

        // BFS
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (farthest >= nums.length - 1) {
                ans++;
                break;
            }
            if (i == end) { // Visited all items on the current level
                ans++; // Increment the level
                end = farthest; // Make the queue size for the next level
            }
        }
        return ans;
    }
}

// Logic:
// 1. Using a search algorithm that works by moving forward in steps and counting each step as a jump.
// 2. The algorithm keeps track of the farthest reachable position at each step and updates the number of jumps
// needed to reach that farthest position.
// 3. The algorithm returns the minimum number of jumps needed to reach the end of the array.
// Complexity :
// Time complexity : O(n)
// Space complexity: O(1)