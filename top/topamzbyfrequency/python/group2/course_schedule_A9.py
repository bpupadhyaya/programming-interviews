"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want
to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Tag: 207/2927 , R175/2935 , R9/50 (amz)
"""

from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    ans = []

    for pair in prerequisites:
        course = pair[0]
        prerequisite = pair[1]
        adj[prerequisite].append(course)
        in_degree[course] += 1

    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        ans.append(current)

        for next_course in adj[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return len(ans) == num_courses


def main():
    num_courses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(can_finish(num_courses, prerequisites))


if __name__ == "__main__":
    main()

"""
Intuition:
The intuition behind this approach is that if there is a cycle in the graph, there will be at least one node that
cannot be visited since it will always have a nonzero in-degree. On the other hand, if there are no cycles, all the
nodes can be visited by starting from the nodes with no incoming edges and removing their outgoing edges one by one.
If all the nodes are visited in the end, it means that it is possible to finish all the courses.

"""