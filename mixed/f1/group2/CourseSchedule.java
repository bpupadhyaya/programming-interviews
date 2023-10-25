// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
// You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first
// if you want to take course a_i.
// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.
// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Sample 1:
// Output: false
// Explanation: There are a total of 2 courses to take.
// To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
// So it is impossible.

import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;
class CourseSchedule {
    public static void main(String...args) {
        int numCourses = 2;
        int[][] prerequisites = {{1,0}, {0,1}};
        System.out.println("Can finish? " + canFinish(numCourses, prerequisites));
    }

    static boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] adj = new List[numCourses];
        int[] inDegree = new int[numCourses];
        List<Integer> ans = new ArrayList<>();

        for (int[] pair: prerequisites) {
            int course = pair[0];
            int prerequisite = pair[1];
            if (adj[prerequisite] == null) {
                adj[prerequisite] = new ArrayList<>();
            }
            adj[prerequisite].add(course);
            inDegree[course]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();
            ans.add(current);

            if (adj[current] != null) {
                for (int next: adj[current]) {
                    inDegree[next]--;
                    if (inDegree[next] == 0) {
                        queue.offer(next);
                    }
                }
            }
        }

        return ans.size() == numCourses;
    }
}