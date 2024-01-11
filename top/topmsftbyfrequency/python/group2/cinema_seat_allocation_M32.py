"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as
shown in the figure above.
Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8]
 means the seat located in row 3 and labelled with 8 is already reserved.
Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four
 adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent,
  but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a
   four-person group in the middle, which means to have two people on each side.

Example:
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already
 reserved and contiguous seats mark with orange are for one group.

Constraints:
1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.

Tag: M32/50
"""
import collections


def max_number_of_families(n: int, reserved_seats: list[list[int]]) -> int:
    # Create a dictionary of sets to store the reserved seats by row
    seats = collections.defaultdict(set)
    # Iterate through the reserved seats
    for i, j in reserved_seats:
        # If the seat is an outside seat in the row, add it to tallies 0 and 1
        if j in {4, 5}:
            seats[i].add(0)
            seats[i].add(1)
        # If the seat is a middle seat in the row, add it to tallies 1 and 2
        elif j in {6, 7}:
            seats[i].add(1)
            seats[i].add(2)
        # If the seat is another type of seat, add it to the corresponding tally
        elif j in {8, 9}:
            seats[i].add(2)
        elif j in {2, 3}:
            seats[i].add(0)
        # Initialize the result to twice the number of rows
        res = 2*n
    # Iterate through the rows of seats
    for i in seats:
        # If a row has all three tallies, subtract two from the result
        if len(seats[i]) == 3:
            res -= 2
        # Otherwise, subtract one from the result
        else:
            res -= 1

    # Return the final result
    return res


def main():
    n = 3
    reserved_seats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    print(max_number_of_families(n, reserved_seats))


if __name__ == "__main__":
    main()
