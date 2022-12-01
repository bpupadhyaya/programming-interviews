//Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e]
// such that sorting this subarray makes the whole array sorted.
// Input -> [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60] Output -> 3, 8
// Alternative problem: Shortest subarray to be removed to make array sorted

class MinLengthSubarrayToSortApp {
    public static void main(String...args) {
        int[] myGivenArray = {10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60};
        int myResult[] = minLenghSubArrayTBS(myGivenArray);
        System.out.println("From "+myResult[0]+" to "+myResult[1]);
    }

    private static int[] minLenghSubArrayTBS(int[] myNums) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;

        boolean flag = false;
        for (int i = 1; i < myNums.length; i++) {
            if (myNums[i] < myNums[i - 1])
                flag = true;
            if (flag)
                min = Math.min(min, myNums[i]);
        }

        flag = false;
        for (int i = myNums.length - 2; i >= 0; i--) {
            if (myNums[i] > myNums[i + 1])
                flag = true;
            if (flag)
                max = Math.max(max, myNums[i]);
        }

        int left, right;
        for (left = 0; left < myNums.length; left++) {
            if (min < myNums[left])
                break;
        }

        for (right = myNums.length - 1; right >= 0; right--) {
            if (max > myNums[right])
                break;
        }
        return new int[]{left, right};
    }

}