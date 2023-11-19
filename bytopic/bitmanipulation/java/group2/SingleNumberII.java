// Given an integer array nums where every element appears three times except for one, which appears exactly once.
// Find the single element and return it.
// You must implement a solution with a linear runtime complexity and use only constant extra space.
// Example:
// Input: nums = [0,1,0,1,0,1,99]
// Output: 99
//
// Tag: 129/150
// Tag: 137/2927, R139/2936 (overall frequency ranking)

class SingleNumberII {
    public static void main(String[] args) {
       int[] nums = {0,1,0,1,0,1,99};
       System.out.println("Single number: " + singleNumber(nums));
    }

    static int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int sum = 0;
            for (int j = 0; j < nums.length; j++) {
                if (((nums[j] >> i) & 1) == 1) {
                    sum++;
                    sum %= 3;
                }
            }
            if (sum != 0) {
                ans |= sum << i;
            }
        }
        return ans;
    }
}

// Method:
// Think about the number in 32 bits and just count how many 1s are there in each bit, and sum %= 3 will clear it once
// it reaches 3. After running for all the numbers for each bit, if we have a 1, then that 1 belongs to the single number,
// we can simply move it back to its spot by doing ans |= sum << i;
//
// This has complexity of O(32n), which is essentially O(n) and very easy to think and implement.
// Als we have a general solution for any times of occurrence. Say all the numbers have 5 times, just do sum %= 5.
