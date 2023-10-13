// Given n non-positive integers representing an elevation map where the width of each bar is 1,
// compute how much water it can trap after raining.
// Sample 1:
// Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
// Output: 6
// Explanation: Visualize each bar and find area that doesn't have outlet. It is the gap between bars.

class TrappingRainWater {
    public static void main(String[] args) {
        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println("Watter trapped: " + trap(height));
    }

    static int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int lmax = Integer.MIN_VALUE;
        int rmax = Integer.MIN_VALUE;
        int ans = 0;

        while (l < r) {
            lmax = Math.max(lmax, height[l]);
            rmax = Math.max(rmax, height[r]);
            ans += (lmax < rmax) ? lmax - height[l++] : rmax - height[r--];
        }
        return ans;
    }
}