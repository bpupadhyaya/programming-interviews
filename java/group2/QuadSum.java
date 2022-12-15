// Given a target and  an array of integers, find arrays of all the unique quadruplets.
// so that their sum is equal to target.
// Sample input: [7,0,-7,0,-9,9], target = 0; sample output: Output: [[-9,-7,7,9],[-9,0,0,9],[-7,0,0,7]]
// Sample input: Input: [5,5,5,5,5], target = 20, Output: [[5,5,5,5]]
// Soln: Time complexity: O(n^3), space complexity: O(n)

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class QuadSum {
    public static void main(String[] args) {
        int[] myInput1 = {7,0,-7,0,-9,9};
        int[] myInput2 = {5,5,5,5,5};
        int t1 = 0;
        int t2 = 20;
        List<List<Integer>> op1 = findQuads(myInput1, t1);
        List<List<Integer>> op2 = findQuads(myInput2, t2);
        for (List<Integer> l1: op1) {
            for (int j = 0; j < l1.size(); j++) {
                System.out.print("," + l1.get(j));
            }
            System.out.println();
        }
        System.out.println("test 2: ");
        for (List<Integer> l2: op2) {
            for (int j = 0; j < l2.size(); j++) {
                System.out.print("," + l2.get(j));
            }
            System.out.println();
        }
    }

    private static List<List<Integer>> findQuads(int[] myInput, int target) {
        Arrays.sort(myInput);
        return kSum(myInput, target, 0, 4);
    }

    private static List<List<Integer>> kSum(int[] myInput, long target, int start, int k) {
        List<List<Integer>> result = new ArrayList<>();

        if (start == myInput.length)
            return result;

        long averageVal = target / k;
        if (myInput[start] > averageVal || averageVal > myInput[myInput.length - 1])
            return result;

        if (k == 2)
            return twoSum(myInput, target, start);

        for (int i = start; i < myInput.length; i++) {
            if (i == start || myInput[i-1] != myInput[i]) {
                for(List<Integer> subset: kSum(myInput, target - myInput[i], i+1, k-1)) {
                    result.add(new ArrayList<>(Arrays.asList(myInput[i])));
                    result.get(result.size() - 1).addAll(subset);
                }
            }
        }
        return result;
    }

    private static List<List<Integer>> twoSum(int[] myInput, long target, int start) {
        List<List<Integer>> result = new ArrayList<>();
        Set<Long> tempStor = new HashSet<>();

        for (int i = start; i < myInput.length; i++) {
            if(result.isEmpty() || result.get(result.size() -1 ).get(1) != myInput[i]) {
                if(tempStor.contains(target - myInput[i])) {
                    result.add(Arrays.asList((int) target - myInput[i], myInput[i]));
                }
            }
            tempStor.add((long) myInput[i]);
        }
        return result;
    }

}