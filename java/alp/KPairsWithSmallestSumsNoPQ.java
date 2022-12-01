// Given two integer arrays array1[] and array2[] sorted in ascending order and an integer k.
// Find k pairs with smallest sums such that one element of a pair belongs to arr1[] and
// other element belongs to array2[]. Input : array1[] = {1, 7, 11}, array2[] = {2, 4, 6}, k = 3
// Output : [1, 2], [1, 4], [1, 6]

import java.util.List;
import java.util.ArrayList;

class KPairsWithSmallestSumsNoPQApp {
    public static void main(String...args) {
        int[] myArray1 = {1, 7, 11};
        int[] myArray2 = {2, 4, 6};
        int k = 3;
        List<int[]> myResult = kPairsWithSmallestSumsNoPQ(myArray1, myArray2, 3);
        for (int[] myArr : myResult) {
            for (int i = 0; i < myArr.length; i++) {
                System.out.print(myArr[i]+",");
            }
            System.out.println();
        }
    }

    private static List<int[]> kPairsWithSmallestSumsNoPQ(int[] myNums1, int[] myNums2, int k) {
        List<int[]> myResult = new ArrayList<int[]>();
        if(myNums1.length == 0 || myNums2.length == 0 || k == 0) {
            return myResult;
        }

        int[] myIndex = new int[myNums1.length];
        while (k-- > 0){
            int mValue = Integer.MAX_VALUE;
            int ind = -1;
            for (int i = 0; i < myNums1.length; i++) {
                if (myIndex[i] >= myNums2.length) {
                    continue;
                }
                if (myNums1[i] + myNums2[myIndex[i]] < mValue) {
                    mValue = myNums1[i] + myNums2[myIndex[i]];
                    ind = i;
                }
            }
            if (ind == -1) {
                break;
            }
            int[] temp = {myNums1[ind], myNums2[myIndex[ind]]};
            myResult.add(temp);
            myIndex[ind]++;
        }
        return myResult;
    }
}