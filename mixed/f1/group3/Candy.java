// There are n children standing in a line. Each child is assigned a rating value given in the
// integer array ratings.
// You are giving candies to these children subjected to the following requirements:
// (a) each child must have at least one candy and
// (b) children with a higher rating get more candies than their neighbors.
// Return the minimum number of candies you need to have to distribute the candies to the children.
// Sample 1:
// Input: ratings = [1,2,2]
// Output: 4
// Explanation: Candie allocation 1, 2, 1

import java.util.Arrays;
class Candy {
    public static void main(String[] args) {
        int[] ratings = {1,0,2};
        System.out.println("Min candies: " + findMinNumberOfCandies(ratings));
    }

    static int findMinNumberOfCandies(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);

        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }

        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1]);
            }
        }

        int totalCandies = 0;
        for(int candy : candies) {
            totalCandies += candy;
        }

        return totalCandies;
    }
}