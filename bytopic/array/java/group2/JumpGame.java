// You are given an integer array nums. You are initially positioned at the array's first index, and each element
// in the array represents your maximum jump length at that position.
// Return true if you can reach the last index, or false otherwise.
// Example:
// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
// Example:
// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
// impossible to reach the last index.
//
// Tag: 9/150
// Tag: 55/2927, R30/2936 (overall frequency ranking)

class JumpGame {
    public static void main(String[] args) {
        int[] nums = {2,3,1,1,4};
        System.out.println(canJump(nums));
    }

    static boolean canJump(int[] nums) {
        int reachable = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reachable)
                return false;
            reachable = Math.max(reachable, i + nums[i]);
        }
        return true;
    }
}

//
// Time complexity ~ O(n)
// Space complexity ~ O(1)
// Logic:
// It suffices that we iterate over each index, and if we ever encounter an index that is not reachable,
// we abort and return false. By the end, we will have iterated to the last index. If the loop finishes,
// then the last index is reachable.