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
// TODO : change variable names to more readable

class JumpGameII {
    public static void main(String[] args) {
        int[] nums = {2,3,1,1,4};
        System.out.println("Min number of jumps: " + jump(nums));
    }

    static int jump(int[] nums) {
        int sc = 0;
        int e = 0;
        int max = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            max = Math.max(max, i + nums[i]);
            if (i == e) {
                sc++;
                e = max;
            }
        }
        return sc;
    }
}

// Logic: