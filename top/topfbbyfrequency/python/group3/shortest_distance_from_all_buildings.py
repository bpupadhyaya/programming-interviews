"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance.
You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according
to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Tag: fb R39/50, 317/2927, R902/2936
Note: program runs but produces wrong output, debug and fix it.
"""


class Solution:
    def __init__(self):
        self.empty, self.building = 0, 1
        self.direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def shortest_distance(self, grid: list[list[int]]) -> int:
        buildings = []
        candidate_lands = {}  # {position, distance}

        # 1. Find all buildings and candidate empty lands
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == self.building:
                    buildings.append((r, c))
                elif grid[r][c] == self.empty:
                    candidate_lands[(r, c)] = 0

        # 2. Compute min distance from each building to all candidate empty lands
        for building_position in buildings:
            self.compute_shortest_distance_bfs(candidate_lands, building_position)

        return min(candidate_lands.values()) if buildings and candidate_lands else -1

    def compute_shortest_distance_bfs(self, candidate_lands: dict, position: (int, int)):
        distance = 0
        visited = set()

        # 1. BFS: this 2-lists bfs traversal makes it possible to avoid storing the distance for each node
        curr_level = [position]
        while curr_level:
            distance += 1

            next_level = []
            for position in curr_level:
                for direction in self.direction:
                    adjacent_position = (position[0] + direction[0], position[1] + direction[1])

                    if adjacent_position in candidate_lands and adjacent_position not in visited:
                        candidate_lands[adjacent_position] += distance

                        visited.add(adjacent_position)
                        next_level.append(adjacent_position)

            curr_level = next_level

            # 2. All empty lands that are not reachable from a building are excluded
            if len(visited) != len(candidate_lands):
                for position in set(candidate_lands.keys()).difference(visited):
                    candidate_lands.pop(position)


def main():
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    soln = Solution()
    result = soln.shortest_distance(grid)
    print('Shortest distance: ', result)


if __name__ == "__main__":
    main()