"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
- numberOfBoxesi is the number of boxes of type i.
- numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Tag: 1710/2927 , R1402/2935 , R39/50 (amz)
"""


def maximum_units(box_types: list[list[int]], truck_size: int) -> int:
    box_types.sort(key=lambda x: x[1], reverse=True)
    s = 0
    for i, j in box_types:
        i = min(i, truck_size)
        s += i * j
        truck_size -= i
        if truck_size == 0:
            break

    return s


def maximum_units_1(box_types: list[list[int]], truck_size: int) -> int:
    box_types = sorted(box_types, key=lambda x: x[1], reverse=True)
    output = 0
    for no, units in box_types:
        if truck_size > no:
            truck_size -= no
            output += (no * units)
        else:
            output += (truck_size * units)
            break
    return output


def main():
    box_types = [[1, 3], [2, 2], [3, 1]]
    truck_size = 4
    print(maximum_units(box_types, truck_size))


if __name__ == "__main__":
    main()
