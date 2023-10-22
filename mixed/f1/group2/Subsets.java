// Given an integer array nums of unique elements, return all possible subsets (the power set).
// The solution set must not contain duplicate subsets. Return the solution in any order.
// Sample 1:
// Input: nums = [1,2,3]
// Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
// Sample 2:
// Input: nums = [0]
// Output: [[],[0]]

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Subsets {
    public static void main(String...args) {
        int[] nums = {1,2,3};
        List<List<Integer>> subsets = findSubsets(nums);
        for (List<Integer> item: subsets) {
            System.out.print(item + ",");
        }
        System.out.println();

    }

    static List<List<Integer>> findSubsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);

        return list;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int start) {
        list.add(new ArrayList<>(tempList));
        for (int i = start; i < nums.length; i++) {
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, i+1);
            tempList.remove(tempList.size() - 1);
        }
    }
}