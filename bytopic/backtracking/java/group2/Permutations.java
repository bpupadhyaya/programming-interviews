// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
// Example:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
//
// Tag: 103/150
// Tag: 46/2927, R160/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
class Permutations {
    public static void main(String...args) {
        int[] nums = {1,2,3};
        List<List<Integer>> result = permute(nums);
        for (List<Integer> perm: result)
            System.out.print(perm + ",");
        System.out.println();
    }

    static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums);

        return list;
    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums) {
        if (tempList.size() == nums.length) {
            list.add(new ArrayList<>(tempList));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (tempList.contains(nums[i]))
                    continue; // element already exists, skip
                tempList.add(nums[i]);
                backtrack(list, tempList, nums);
                tempList.remove(tempList.size() - 1);
            }
        }
    }
}