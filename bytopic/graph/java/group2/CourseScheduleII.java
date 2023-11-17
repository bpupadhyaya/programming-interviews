// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
// prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
// If it is impossible to finish all courses, return an empty array.
// Example:
// Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
// Output: [0,2,1,3]
// Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
// Both courses 1 and 2 should be taken after you finished course 0.
// So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
//
// Tag: 94/150
// Tag: 210/2927, R303/2936 (overall frequency ranking)

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.BitSet;
import java.util.ArrayDeque;
import java.util.Deque;
class CourseScheduleII {
    public static void main(String...args) {
        int numCourses = 4;
        int[][] prerequisites = {{1,0},{2,0},{3,1},{3,2}};
        int[] ordering = findOrder(numCourses, prerequisites);
        System.out.println("Ordering: " + Arrays.toString(ordering));
    }

    static int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] incLinkCounts = new int[numCourses];
        List<List<Integer>> adjs = new ArrayList<>(numCourses);
        initializeGraph(incLinkCounts, adjs, prerequisites);
        return solveByDFS(adjs);
    }

    private static void initializeGraph(int[] incLinkCounts, List<List<Integer>> adjs, int[][] prerequisites) {
        int n = incLinkCounts.length;
        while (n-- > 0)
            adjs.add(new ArrayList<>());
        for (int[] edge: prerequisites) {
            incLinkCounts[edge[0]]++;
            adjs.get(edge[1]).add(edge[0]);
        }
    }

    private static int[] solveByDFS(List<List<Integer>> adjs) {
        BitSet hasCycle = new BitSet(1);
        BitSet visited = new BitSet(adjs.size());
        BitSet onStack = new BitSet(adjs.size());
        Deque<Integer> order = new ArrayDeque<>();
        for (int i = adjs.size() - 1; i >= 0; i--) {
            if (visited.get(i) == false && hasOrder(i, adjs, visited, onStack, order) == false)
                return new int[0];
        }
        int[] orderArray = new int[adjs.size()];
        for (int i = 0; !order.isEmpty(); i++)
            orderArray[i] = order.pop();
        return orderArray;
    }

    private static boolean hasOrder(int from, List<List<Integer>> adjs, BitSet visited, BitSet onStack,
                                    Deque<Integer> order) {
        visited.set(from);
        onStack.set(from);
        for (int to: adjs.get(from)) {
            if (visited.get(to) == false) {
                if (hasOrder(to, adjs, visited, onStack, order) == false)
                    return false;
            } else if (onStack.get(to) == true) {
                return false;
            }
        }
        onStack.clear(from);
        order.push(from);

        return true;
    }
}
