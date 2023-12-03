"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first
if you want to take course a_i.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Sample 1:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Tag: 93/150
Tag: 207/2927, R175/2936 (overall frequency ranking)
"""
from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    ans = []

    for pair in prerequisites:
        course = pair[0]
        prerequisites = pair[1]
        adj[prerequisites].append(course)
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
