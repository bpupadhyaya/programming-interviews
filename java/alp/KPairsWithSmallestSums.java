// Given two integer arrays array1[] and array2[] sorted in ascending order and an integer k.
// Find k pairs with smallest sums such that one element of a pair belongs to arr1[] and
// other element belongs to array2[]. Input : array1[] = {1, 7, 11}, array2[] = {2, 4, 6}, k = 3
// Output : [1, 2], [1, 4], [1, 6]

import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Pair {
    int[] myArray;
    public Pair(int x, int y) {
        myArray = new int[2];
        myArray[0] = x;
        myArray[1] = y;
    }
}
class KPairsWithSmallestSumsApp {
    public static void main(String...args) {
        int[] myArray1 = {1, 7, 11};
        int[] myArray2 = {2, 4, 6};
        int k = 3;
        List<List<Integer>> myResult = kPairsWithSmallestSums(myArray1, myArray2, 3);
        System.out.println(myResult);
    }

    private static List<List<Integer>> kPairsWithSmallestSums(final int[] myNums1, final int[] myNums2, int k) {
        List<List<Integer>> myResult = new ArrayList<List<Integer>>();
        int m = myNums1.length;
        int n = myNums2.length;
        PriorityQueue<Pair> myPair = new PriorityQueue<Pair>((a,b) ->
                ((myNums1[a.myArray[0]] + myNums2[a.myArray[1]]) - (myNums2[b.myArray[1]] + myNums1[b.myArray[0]])));
        for(int i=0; i<m && i<k; i++)
            myPair.add(new Pair(i, 0));
        while(k-->0 && !myPair.isEmpty()) {
            Pair x = myPair.poll();
            List<Integer> myArray = new ArrayList<>();
            myArray.add(myNums1[x.myArray[0]]);
            myArray.add(myNums2[x.myArray[1]]);
            myResult.add(myArray);
            x.myArray[1] += 1;
            if(x.myArray[1] < n)
                myPair.add(new Pair(x.myArray[0], x.myArray[1]));
        }
        return myResult;
    }
}