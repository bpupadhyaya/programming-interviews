"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi]
 indicates that there is a bidirectional road between cities ai and bi.
The network rank of two different cities is defined as the total number of directly connected roads to either city.
 If a road is directly connected to both cities, it is only counted once.
The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1.
The road between 0 and 1 is only counted once.

Constraints:
2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
Each pair of cities has at most one road connecting them.

Tag: M16/50
"""


def maximal_network_rank(n: int, roads: list[list[int]]) -> int:
    # Counts of roads connected to each city
    connections = [0] * n

    # 2D boolean array to check if a road exists between two cities
    road_exists = [[False] * n for _ in range(n)]

    for a, b in roads:
        connections[a] += 1
        connections[b] += 1
        road_exists[a][b] = road_exists[b][a] = True

    max_rank = 0

    # Iterate through each pair of cities
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate current rank
            current_rank = connections[i] + connections[j] - road_exists[i][j]
            # Update max rank if current is higher
            max_rank = max(max_rank, current_rank)

    return max_rank


def main():
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(maximal_network_rank(n, roads))


if __name__ == "__main__":
    main()
