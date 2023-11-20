"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of
the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without
obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Tag: fb R16/50, 1762/2927, R271/2936
"""

from collections import deque
def findBuildings(heights: list[int]) -> list[int]:
    result = [len(heights) - 1]
    for i in range(len(heights) - 2, -1, -1):
        if heights[i] > heights[result[-1]]:
            result.append(i)
    result.reverse()
    return result

def findBuildings1(heights: list[int]) -> list[int]:
    result = deque([len(heights) - 1])
    for i in range(len(heights) - 2, -1, -1):
        if heights[i] > heights[result[0]]:
            result.appendleft(i)
    return result

def main():
    heights = [4,2,3,1]
    print('Building with ocean view: ', findBuildings1(heights))

if __name__ == "__main__":
    main()
