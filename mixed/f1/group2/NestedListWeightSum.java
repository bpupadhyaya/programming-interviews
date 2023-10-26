// You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may
// also be integers or other lists.
// The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1]
// has each integer's value set to its depth.
// Return the sum of each integer in nestedList multiplied by its depth.
// Sample 1:
// Input: nestedList = [[1,1],2,[1,1]]
// Output: 10
// Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
// Note: work on fixing testing code. Probably the main logic is complete.

import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;
public class NestedInteger {
    List<NestedInteger> nestedList = null;
    int value = 0;
    // Constructor initializes an empty nested list.
    public void NestedInteger() {
        nestedList = new ArrayList<>();
    }
    // Constructor initializes a single integer.
    public void NestedInteger(int value) {
        this.value = value;
    }
    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger() {
        if (nestedList == null)
            return true;
    }
    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger() {
        if (nestedList != null)
            return null;
        return value;
    }
    // Set this NestedInteger to hold a single integer.
    public void setInteger(int value) {
        this.value = value;
    }
    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    public void add(NestedInteger ni) {
        if (nestedList == null)
            nestedList = new ArrayList<>();
        nestedList.add(ni);
    }
    // @return the nested list that this NestedInteger holds, if it holds a nested lis
    // Return empty list if this NestedInteger holds a single integer
    public List<NestedInteger> getList() {
        return nestedList;
    }
}

class NestedListWeightSum {
    static int total = 0;
    public static void main(String...args) {
        List l1 = new ArrayList<>();
        l1.add(1);
        l1.add(1);
        NestedInteger nestedList = new NestedInteger();
        nestedList.add(l1);

        NestedInteger nval1 = new NestedInteger(2);
        nestedList.add(nval1);

        List l2 = new ArrayList<>();
        l1.add(1);
        l1.add(1);
        nestedList.add(l2);

        System.out.println("Nested list weight sum: " + depthSum(nestedList));
    }

    static int depthSum(List<NestedInteger> nestedList) { // DFS
        callDepthSum(nestedList, 1);
        return total;
    }

    private static void callDepthSum(List<NestedInteger> nl, int depth) {
        for (NestedInteger ni: nl) {
            if (ni.isInteger()) {
                total += ni.getInteger() * depth;
            } else {
                List<NestedInteger> list = ni.getList();
                callDepthSum(list, depth + 1);
            }
        }
    }

    static int depthSumBFS(List<NestedInteger> nestedList) {
        int sum = 0, depth = 1;

        Queue<NestedInteger> q = new LinkedList<>();
        q.addAll(nestedList);

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                NestedInteger ni = q.poll();
                if (ni.isInteger())
                    sum += ni.getInteger() * depth;
                else
                    q.addAll(ni.getList());
            }
            depth++;
        }
        return sum;
    }
}