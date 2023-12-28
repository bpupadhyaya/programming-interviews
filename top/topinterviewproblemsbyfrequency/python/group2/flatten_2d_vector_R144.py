"""
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
Implement the Vector2D class:
- Vector2D(int[][] vec) initializes the object with the 2D vector vec.
- next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that
all the calls to next are valid.
- hasNext() returns true if there are still some elements in the vector, and false otherwise.

Example:
Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False

Constraints:
0 <= vec.length <= 200
0 <= vec[i].length <= 500
-500 <= vec[i][j] <= 500
At most 10^5 calls will be made to next and hasNext.

Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.

R144/145
"""


class Vector2D:
    def __init__(self, vec: list[list[int]]):
        self.vec = vec
        self.col = 0
        self.row = 0

    def next(self) -> int:
        self.has_next()
        val = self.vec[self.row][self.col]
        self.col += 1
        return val

    def has_next(self) -> bool:
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            self.row += 1
            self.col = 0

        return False


def main():
    vector2d = Vector2D([[1, 2], [3], [4]]);
    print(vector2d.next())      # return 1
    print(vector2d.next())      # return 2
    print(vector2d.next())      # return 3
    print(vector2d.has_next())  # return True
    print(vector2d.has_next())  # return True
    print(vector2d.next())      # return 4
    print(vector2d.has_next())  # return False


if __name__ == "__main__":
    main()
