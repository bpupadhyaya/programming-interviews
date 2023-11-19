// You are given an integer array coins representing coins of different denominations and an integer amount
// representing a total amount of money.
// Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
// any combination of the coins, return -1.
// You may assume that you have an infinite number of each kind of coin.
// Example:
// Input: coins = [1,2,5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1
//
// Tag: 140/150
// Tag: 322/2927, R324/2936 (overall frequency ranking)

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Set;
import java.util.HashSet;
class CoinChange {
    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.println("Fewest number of coins: " + coinChange(coins, amount));
    }

    static int coinChange(int[] coins, int amount) {
          if (coins == null || coins.length == 0 || amount < 1) return 0;

          Deque<Integer> queue = new ArrayDeque<Integer>();
          Set<Integer> visited = new HashSet<Integer>();
          queue.addFirst(amount);
          visited.add(amount);
          int level = 0;

          while (!queue.isEmpty()) {
              int size = queue.size();

              while (size-- > 0) {
                  int curr = queue.removeLast();
                  if (curr == 0) return level;
                  if (curr < 0) continue;

                  for (int coin: coins) {
                      int next = curr - coin;
                      if (next >= 0 && !visited.contains(next)) {
                          queue.addFirst(next);
                          visited.add(next);
                      }
                  }
              }
              level++;
          }

          return -1;
    }
}

// Logic:
// BFS soln:
// Basic idea is to substract/remove each of the coins from the total amount, which will result in coins.length different
// amounts. Keep doing the same to them until you find 0. Some key things to keep in mind:
// 1. Ignore when your diff goes below 0
// 2. Memoize using a visited set so that you don't re-calculate the branches of the graph that you've already seen once