// Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
// You may return the answer in any order.
// Example:
// Input: n = 4, k = 2
// Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
// Explanation: There are 4 choose 2 = 6 total combinations.
// Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
//
// Tag: 102/150
// Tag: 77/2927, R335/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
class Combinations {
    public static void main(String[] args) {
        int n = 4;
        int k = 2;
        List<List<Integer>> combinations = combine(4, 2);
        for (List<Integer> combination: combinations)
            System.out.print(combination + ",");
        System.out.println();
    }

    static List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(n, k, 1, new ArrayList<>(), result);

        return result;
    }

    private static void backtrack(int n, int k, int start, List<Integer> combination, List<List<Integer>> result) {
        if (combination.size() == k) {
            result.add(new ArrayList<>(combination));
            return;
        }
        for (int i = start; i <=n; i++) {
            combination.add(i);
            backtrack(n, k, i+1, combination, result);
            combination.remove(combination.size() -1);
        }
    }
}