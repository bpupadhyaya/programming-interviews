// Given: An array of integers, a target integer value, say z
// To find: Indices of two numbers, say x and y, such that x + y = z
// Assumptions: Each input has exactly one solution; may not use the same element twice; answer
//              can be returned in any order

import java.util.Map;
import java.util.HashMap;

class TargetSum {
    public static void main(String...args) {
        int[] myNums = {10, 30, 25, 5, 15, 15, 15, 70};
        int myTarget = 30;
        int[] myResult = targetSum(myNums, myTarget);
        if (myResult != null) {
            System.out.println(myResult[0]+", "+myResult[1]);
        } else {
            System.out.println("Such a pair doesn't exist!");
        }
    }

    private static int[] targetSum(int[] myNums, int myTarget) {
        Map<Integer, Integer> myMap = new HashMap<>();
        for(int i = 0; i < myNums.length; i++) {
            int compl = myTarget - myNums[i];
            if (myMap.containsKey(compl)) {
                return new int[] {myMap.get(compl), i};
            }
            myMap.put(myNums[i], i);
        }
        return null; // such pair doesn't exist
    }
}
