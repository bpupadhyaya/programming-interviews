"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return
any of them.
If it is impossible to finish all courses, return an empty array.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Tag: R89/145
Tag: 94/150
Tag: 210/2927, R303/2936 (overall frequency ranking), M23/50
"""
from collections import defaultdict, deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # Topological sort based solution
    # Dependency of each node/course
    _ = [0] * num_courses

    result = []
    # Adjacency list
    mapper = defaultdict(list)

    # Putting all the courses that don't have any dependency in queue
    for ai, bi in prerequisites:
        mapper[bi].append(ai)
        _[ai] += 1

    q = deque()

    for i in range(len(_)):
        if _[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        result.append(node)
        for neigh in mapper[node]:
            # One less dependency
            _[neigh] -= 1
            if _[neigh] == 0:
                q.append(neigh)
    if len(result) == num_courses:
        return result
    return []


def main():
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(find_order(num_courses, prerequisites))


if __name__ == "__main__":
    main()
