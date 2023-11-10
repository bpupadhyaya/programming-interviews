// There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
// You are giving candies to these children subjected to the following requirements:
// Each child must have at least one candy.
// Children with a higher rating get more candies than their neighbors.
// Return the minimum number of candies you need to have to distribute the candies to the children.
// Example:
// Input: ratings = [1,2,2]
// Output: 4
// Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
// The third child gets 1 candy because it satisfies the above two conditions.
// Tag: 15/150

class Candy {
    public static void main(String[] args) {
        int[] ratings = {1,2,2};
        System.out.println("Min. number of candies: " + candy(ratings));
    }

    static int candy(int[] ratings) {
        if (ratings.length == 0) return 0;
        int ret = 1;
        int up = 0, down = 0, peak = 0;

        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i-1] < ratings[i]) {
                peak = ++up;
                down = 0;
                ret += 1 + up;
            } else if (ratings[i-1] == ratings[i]) {
                peak = up = down = 0;
                ret += 1;
            } else {
                up = 0;
                down++;
                ret += 1 + down + (peak >= down ? -1 : 0);
            }
        }
        return ret;
    }
}